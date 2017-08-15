t = [-10, -8, 0, 1, 2, 5, -2, -4]
maxima = t[0]
minima = t[0]
for x in t:
    if x > maxima:
        maxima = x
    if x < minima:
        minima = x
print("MAX: {:4}".format(maxima))
print("MIN: {:4}".format(minima))