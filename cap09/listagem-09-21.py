from os import path
from time import ctime
from sys import argv

nome = argv[1]
print(f"Nome: {nome}")
tamanho = path.getsize(nome)
print(f"Tamanho: {tamanho}")
criado = ctime(path.getctime(nome))
print(f"Criado: {criado}")
modificado = ctime(path.getmtime(nome))
print(f"Modificado: {modificado}")
acessado = ctime(path.getatime(nome))
print(f"Acessado: {acessado}")
