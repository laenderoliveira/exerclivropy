import sys


print("Números de parâmetros: {}".format(len(sys.argv)))
for n, p in enumerate(sys.argv):
    print("[{}] = {}".format(n, p))
