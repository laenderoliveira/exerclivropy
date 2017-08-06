while True:
    op = input("(+) (-) (*) (/) ou (0) para sair: ")
    if op == "0":
        print("Você escolheu sair!")
        break
    x = 1
    while x <= 10:
        y = 1
        while y <= 10:
            if op == "+":
                r = x + y
                print("{} + {} = {}".format(x, y, r))
            elif op == "-":
                r = x - y
                print("{} - {} = {}".format(x, y, r))
            elif op == "*":
                r = x * y
                print("{} * {} = {}".format(x, y, r))
            elif op == "/":
                r = x / y
                print("{} / {} = {}".format(x, y, r))
            else:
                print("Operação inválida!")
                x = 11
                break
            y += 1
        x += 1