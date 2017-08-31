def fibonacci(n):
    if n == 0:
        return 0
    fib = [0, 1]
    for x in range(n):
        fib.append(fib[x] + fib[x+1])
    return fib[x+1]
for x in range(22):
    print("F({0:02})= {1:>5}".format(x, fibonacci(x)))