import setuptools


with open("README.md", encoding="utf8") as f:
    readme = f.read()


setuptools.setup(
    name="libertem-jupyter-proxy",
    version="0.1.1",
    url="https://github.com/LiberTEM/LiberTEM-jupyter-proxy",
    author="",
    license="BSD",
    description="Run LiberTEM via JupyterLab/JupyterHub",
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    keywords=["Jupyter"],
    classifiers=["Framework :: Jupyter"],
    install_requires=[
        'jupyter-server-proxy',
    ],
    entry_points={
        "jupyter_serverproxy_servers": [
            "libertem = libertem_jupyter_proxy:setup_libertem",
        ]
    },
    package_data={"libertem_jupyter_proxy": ["icons/*", "share/*"]},
    project_urls={},
)
