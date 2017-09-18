import sys


if len(sys.argv) != 4:
    print("Uso: python exercicio-09-02.py nome_do_arquivo inicio fim\n")
else:
    file_name = sys.argv[1]
    start = int(sys.argv[2])
    end = int(sys.argv[3])
    file = open(file_name, "r")
    rows = file.readlines()
    for row in rows[start:end+1]:
        print(row[:-1])
    file.close()
