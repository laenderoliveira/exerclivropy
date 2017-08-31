def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b)
print("Maior divisor comum MDC:", mdc(12, 9))