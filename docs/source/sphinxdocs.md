# Docs with Sphinx and GitHub Pages

Documents can be generated based on the sphinx tool.

## Setup

```sh
$ sphinx-quickstart ./docs
$ sphinx-apidoc -f -o docs/source pyskelton
$ sphinx-build -a docs/source/ docs
```

## To See on GitHub Pages

sphinx.ext.githubpages

## To See on Read The Docs

.readthedocs.yaml
