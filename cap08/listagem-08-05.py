def pesquise(lista, valor):
    for x, e in enumerate(lista):
        if e == valor:
            return x
    return None

lista = [12, 45, 75, 34]
print(pesquise(lista, 75))
