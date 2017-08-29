def pesquise(lista, valor):
    if valor in lista:
        return lista.index(valor)
    return None

l = [12, 45, 67, 98, 32]
print(pesquise(l, 98))
print(pesquise(l, 22))