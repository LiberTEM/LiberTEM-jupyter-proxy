import os
import sys
import json
import shutil


def _get_libertem_path():
    config_path = os.path.join(sys.prefix, "etc", "jupyter_libertem_proxy.json")
    if os.path.exists(config_path):
        with open(config_path, "r") as f:
            config = json.loads(f.read())
        path = config.get('libertem_server_path')
        if path is not None:
            return path

    executable = "libertem-server"
    if shutil.which(executable):
        return executable

    raise FileNotFoundError("Can not find libertem-server in configuration or PATH")


def _get_libertem_cmd(port):
    path = _get_libertem_path()

    cmd = [
        path,
        "--no-browser",
        "--port=" + str(port),
    ]

    return cmd



def setup_libertem():
    return {
        "command": _get_libertem_cmd,
        "timeout": 20,
        "new_browser_tab": True,
        "launcher_entry": {
            "title": "LiberTEM",
            "icon_path": os.path.join(
                os.path.dirname(os.path.abspath(__file__)), "icons", "libertem.svg"
            ),
        },
    }
