# Run the LiberTEM GUI in JupyterLab / JupyterHub

## Install locally

1. Clone this repo

    $ git clone https://github.com/sk1p/libertem-jupyter-proxy

2. Install dependencies and LiberTEM master:

    $ pip install -e .
    
    $ pip install -e "git+https://github.com/liberTEM/LiberTEM/#egg=libertem"

3. Start jupyter-lab or jupyter-notebook

    $ jupyter-lab

or

    $ jupyter notebook

Now LiberTEM should be available as an icon in JupyterLab, or in the
"New" dropdown in the classical notebook interface / JupyterHub.

## Try it (WIP)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/sk1p/libertem-jupyter-proxy/master?urlpath=lab)

## Thanks

Mostly stolen from https://github.com/betatim/vscode-binder
