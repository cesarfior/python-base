#!/usr/bin/env python3
"""
Document my program
Dependendo da linguagem do ambeinte o programa vai executar
ex se nao tiver configurada 
export LANG=pt_BR
"""
__version__ = "0.0.1"
__author__ = "Cesar Fior"
__licence__ = "Unlicense"
current_language = "en_US"
msg = "hello"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"

print(msg)
