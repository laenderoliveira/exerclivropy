import os.path
dir = "temp"
if os.path.isdir(dir):
    print("Diretório temp existe")
elif os.path.isfile(dir):
    print("Arquivo temp existe")
else:
    print("Diretório temp não existe")