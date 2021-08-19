# Run the LiberTEM GUI in JupyterLab / JupyterHub

See [the LiberTEM docs](https://libertem.github.io/LiberTEM/jupyter.html) for details.

## Install

1. Clone this repo

    $ git clone https://github.com/LiberTEM/LiberTEM-jupyter-proxy

2. Install dependencies and LiberTEM master:

    $ pip install -e .
    
    $ pip install -e "git+https://github.com/liberTEM/LiberTEM/#egg=libertem"

3. Start jupyter-lab or jupyter-notebook

    $ jupyter-lab

or

    $ jupyter notebook

Now LiberTEM should be available as an icon in JupyterLab, or in the
"New" dropdown in the classical notebook interface / JupyterHub.

## Deployment notes

When deploying behind a reverse proxy, make sure websocket requests are
proxied for all URLs, not just for specifically matching ones. Otherwise, something
like connecting to `wss://<hostname>/user/<username>/libertem/events/` will fail
with 400 bad request, as `Upgrade: websocket` is not supported.

## Try it (WIP)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/LiberTEM/LiberTEM-jupyter-proxy/master?urlpath=lab)

## Thanks

Mostly stolen from https://github.com/betatim/vscode-binder
