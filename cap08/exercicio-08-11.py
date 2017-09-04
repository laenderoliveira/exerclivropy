def f_str(string, minimum, maximum):
    size = len(string)
    return minimum <= size <= maximum

print(f_str("laender", 0, 10))