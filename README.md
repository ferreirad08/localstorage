# Pylocalstorage

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/ferreirad08/pylocalstorage/blob/main/LICENSE)
[![PyPI version](https://badge.fury.io/py/pylocalstorage.svg)](https://badge.fury.io/py/pylocalstorage)
![Tests](https://github.com/ferreirad08/pylocalstorage/actions/workflows/tests.yml/badge.svg)
![Custom badge](https://img.shields.io/endpoint?url=https%3A%2F%2Fjsonblob.com%2Fapi%2FjsonBlob%2F1002315458195767296)
[![Downloads](https://pepy.tech/badge/pylocalstorage/month)](https://pepy.tech/project/pylocalstorage)

A package to store data on the hard disk (HD) and make it available to all Python applications running locally!

## Requirements
* `Python 2.7 or higher`

## Installation

Simply install pylocalstorage package from [PyPI](https://pypi.org/project/pylocalstorage/)

```bash
$ pip install pylocalstorage
```

## Examples

```python
>>> from pylocalstorage import LocalStorage
>>> ls = LocalStorage()
>>> ls.setItem("name", "David")
>>> ls.setItem("age", 29)
>>> ls.setItem("address", {"country": "Brazil", "city": "Manaus"})
>>> ls.length
3
>>> ls.setItem("name", "David Ferreira")
>>> ls.getItem("name")
'David Ferreira'
>>> ls.removeItem("name")
>>> ls.key(0)
'age'
>>> ls.key(1)
'address'
>>> ls.clear()
>>> ls.length
0
```
