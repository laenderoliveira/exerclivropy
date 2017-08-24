primeira = input("Primeira String: ")
segunda = input("Segunda String: ")
terceira = input("Terceira String: ")
r = ""
if len(segunda) == len(terceira):
    for letra in primeira:
        if letra in segunda:
            posicao = segunda.find(letra)
            r += terceira[posicao]
        else:
            r += letra
print(r)