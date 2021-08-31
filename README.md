# Run the LiberTEM GUI in JupyterLab / JupyterHub

See [the LiberTEM docs](https://libertem.github.io/LiberTEM/jupyter.html) for more details!

## Requirements
- Python 3.6+
- Jupyter Notebook 6.0+
- JupyterLab 2.1+
- LiberTEM 0.8.0+

## LiberTEM
[LiberTEM](https://libertem.github.io/LiberTEM/index.html) is an open source platform for high-throughput distributed processing of large-scale binary data sets and live data streams using a modified MapReduce programming model.
The current focus is pixelated scanning transmission electron microscopy (STEM) and scanning electron beam diffraction data.


## Install

1. Install this package and LiberTEM:

    $ pip install libertem-jupyter-proxy libertem

2. enable `jupyter-server-proxy` extension

For Jupyter Classic, activate the jupyter-server-proxy extension:
```
jupyter serverextension enable --sys-prefix jupyter_server_proxy
```

For JupyterLab, install the @jupyterlab/server-proxy extension:
```
jupyter labextension install @jupyterlab/server-proxy
jupyter lab build
```

4. Start jupyter-lab or jupyter-notebook

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

If you want to customize the startup of LiberTEM, you can drop a JSON file into
`$PREFIX/etc/libertem_jupyter_proxy.json`, with contents like this:

```json
{"libertem_server_path": "/path/to/a/venv/bin/libertem-server"}
```

This allows to install LiberTEM itself into a different Python environment
than Jupyter, as opposed to using the same environment as in the example above.
It can also allow to write a wrapper script to customize the environment setup, as in the example script
`libertem_jupyter_proxy/share/launch_juwels.sh`

Without configuration, `libertem-server` is expected to be found in `$PATH`.

## Try it (WIP)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/LiberTEM/LiberTEM-jupyter-proxy/master?urlpath=lab)

## Thanks

Mostly stolen from https://github.com/betatim/vscode-binder
