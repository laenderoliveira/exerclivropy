def f_int(question, minimum, maximum):
    while True:
        value = int(input(question))
        if value < minimum or value > maximum:
            print("Invalid value! Enter a value between {} and {}".format(minimum, maximum))
        else:
            return value

x = f_int("Enter a value:", 0, 10)
print(x)