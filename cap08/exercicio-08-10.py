def fibonacci(n):
    fib = [0, 1]
    for x in range(n):
        fib.append(fib[x] + fib[x+1])
    return fib[x]

print(fibonacci(7))