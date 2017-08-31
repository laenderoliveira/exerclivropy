def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Digite para achar o N da sequencia de fibonacci: "))
print(fibonacci(n - 1))