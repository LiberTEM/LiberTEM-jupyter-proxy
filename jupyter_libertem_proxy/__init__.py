import os
import shutil


def setup_libertem():
    def _get_libertem_cmd(port):
        executable = "libertem-server"
        if not shutil.which(executable):
            raise FileNotFoundError("Can not find libertem-server in PATH")

        cmd = [
            executable,
            "--no-browser",
            "--port=" + str(port),
        ]

        return cmd

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
