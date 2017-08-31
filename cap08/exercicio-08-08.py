def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b)

def mmc(a, b):
    return abs(a*b) / mdc(a, b)
print("Maior divisor comum MDC:", mdc(12, 9))
print("Menor multiplo comum MMC:", mmc(12, 9))