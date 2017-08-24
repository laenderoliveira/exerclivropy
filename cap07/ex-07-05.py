primeira = input("Primeira String: ")
segunda = input("Segunda String: ")
r = ""

for letra in primeira:
    if letra not in segunda:
        r += letra
print(r)