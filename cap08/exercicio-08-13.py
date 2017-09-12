from random import randint


n = randint(1, 10)

for _ in range(3):
    t = int(input("Tente 1 número entre 1 e 10: "))
    if n == t:
        print("Acerto Mizeravi!")
        break
    else:
        print("Erroouuuuu!")
else:
    print("Fim de jogo! O número certo é %d!" % n)
