# pymysc

Miscellaneous things relating with Python coding.
Components:
- README.md
- pyskelton/
- docs/
    - pyskelton package
    - tips
    - idea note
- setup.py
- notebook/
    - ipynb

## setup for pyskelton and sphinx

(for bash on mac)
```sh
$ python3.8 -m venv venv
$ . ./venv/bin/activate
$ pip install sphinx sphinx-rtd-theme myst-parser nbsphinx
```

# pyskelton

Python project skelton

# docs

To see on GitHub Pages

sphinx-quickstart ./docs
sphinx-apidoc -f -o docs/source pyskelton
sphinx-build docs/source/ docs