from os import path
from sys import argv
dir = argv[1]
if path.isdir(dir):
    print(f"Diretório: {dir}")
elif path.isfile(dir):
    print(f"Arquivo: {dir}")
else:
    print(f"{dir} não existe")