import os
import sys
import json
import shutil
import secrets
import logging
from tempfile import mkdtemp


logger = logging.getLogger(__name__)
logger.setLevel('INFO')


def _get_libertem_path():
    """
    Gets the path to libertem-server or a wrapper script from config files:

    - {LIBERTEM_ROOT}/etc/libertem_jupyter_proxy.json
    - {sys.prefix}/etc/libertem_jupyter_proxy.json

    If no config is found, looks up 'libertem-server' in the $PATH.
    """
    prefix = os.environ.get("LIBERTEM_ROOT", sys.prefix)
    config_path = os.path.join(prefix, "etc", "libertem_jupyter_proxy.json")
    path = None

    # first, look up path in config:
    if os.path.exists(config_path):
        with open(config_path, "r") as f:
            config = json.loads(f.read())
        path = config.get('libertem_server_path')

    # if there is no config, or the config doesn't contain the key,
    # check $PATH:
    if path is None:
        path = shutil.which("libertem-server")

    if path is None:
        raise FileNotFoundError("Could not find libertem-server in configuration or PATH")

    return path


def make_get_libertem_cmd(token_path):
    def _get_libertem_cmd(port):
        path = _get_libertem_path()

        cmd = [
            path,
            "--no-browser",
            "--port=" + str(port),
            "--token-path=" + str(token_path),
        ]

        logger.info('LiberTEM command: %s', ' '.join(cmd))

        return cmd
    return _get_libertem_cmd


def make_token():
    return secrets.token_urlsafe(32)


def store_token(token):
    """
    Make a temporary directory with access limited to the current user,
    and store the token in a new file in that directory.

    Returns the path to the token file.
    """
    # mkdtemp makes sure the directory is only readable by the current user:
    token_dir = mkdtemp(prefix="libertem")
    token_path = os.path.join(token_dir, 'libertem-server-token')
    with open(token_path, 'w') as f:
        f.write(token)
    return token_path


def setup_libertem():
    token = make_token()
    token_path = store_token(token)

    return {
        "command": make_get_libertem_cmd(token_path),
        "timeout": 90,
        "request_headers_override": {
            "X-Api-Key": token,
        },
        "new_browser_tab": True,
        "launcher_entry": {
            "title": "LiberTEM",
            "icon_path": os.path.join(
                os.path.dirname(os.path.abspath(__file__)), "icons", "libertem.svg"
            ),
        },
    }
