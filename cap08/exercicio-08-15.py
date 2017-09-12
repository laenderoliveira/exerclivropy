lista = ["a", ["b", "c"], "d", ["e", "f"]]
tamanho = len(lista) - 1


def imprime(lista, tamanho):
    if tamanho == 0:
        return lista[0]
    else:
        print(lista[tamanho])
        return imprime(lista, tamanho - 1)


print(imprime(lista, tamanho))
