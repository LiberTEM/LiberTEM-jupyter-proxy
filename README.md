# Run LiberTEM in JupyterLab

## Install locally

1. Clone this repo

    $ git clone https://github.com/sk1p/libertem-jupyter-proxy

2. Install dependencies and LiberTEM master:

    $ pip install -e .
    $ pip install -e "git+https://github.com/liberTEM/LiberTEM/#egg=libertem"

3. Enable and install server-proxy extension:

    $ jupyter serverextension enable --py jupyter_server_proxy
    $ jupyter labextension install @jupyterlab/server-proxy

3. Start jupyter-lab

    $ jupyter-lab

## Try it (WIP)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/sk1p/libertem-jupyter-proxy/master?urlpath=lab)

## Thanks

Mostly stolen from https://github.com/betatim/vscode-binder
