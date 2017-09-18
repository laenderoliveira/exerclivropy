import sys


if len(sys.argv) != 2:
    print("Uso: python exercicio-09-01.py nome_do_arquivo\n")
else:
    file_name = sys.argv[1]
    file = open(file_name, "r")
    for row in file.readlines():
        print(row[:-1])
    file.close()
