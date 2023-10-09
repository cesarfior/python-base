#!/usr/bin/env python3
"""
Document my program
Dependendo da linguagem do ambeinte o programa vai executar
ex se nao tiver configurada 
export LANG=pt_BR.utf8
"""
__version__ = "0.0.1"
__author__ = "Cesar Fior"
__licence__ = "Unlicense"

import os
current_language = os.getenv("LANG")[:5]
msg = "hello"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"

print(msg)
