# localstorage

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/ferreirad08/localstorage/blob/main/LICENSE)

A package to store data on hard disk (HD) and make it available to all Python applications running in parallel!

## Requirements
* `python 3`

## Installation

Simply install localstorage package from [PyPI](https://pypi.org/project/localstorage/)

    pip install localstorage

## Examples

    from localstorage import LocalStorage

    # Conectando ao LocalStorage
    my_storage = LocalStorage()

    # Criando três itens
    my_storage.setItem("name", "David")
    my_storage.setItem("country", "Brazil")
    my_storage.setItem("city", "Manaus")
    print(my_storage.length)

    # Atualizando um item
    my_storage.setItem("name", "David Ferreira")

    # Obtendo um item
    print(my_storage.getItem("name"))

    # Removendo um item
    my_storage.removeItem("city")
    print(my_storage.getItem("city"))

    # Recuperando todas as chaves existentes
    for i in range(my_storage.length):
        print(my_storage.key(i))

    # Limpando o LocalStorage
    my_storage.clear()
    print(my_storage.length)
