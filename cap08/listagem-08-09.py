def fatorial(x):
    fat = 1
    while x > 1:
        fat *= x
        x -= 1
    return fat

print(fatorial(0))