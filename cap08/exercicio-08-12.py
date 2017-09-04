def str_in_list(string, list_):
    return string in list_

s = "laender"
l = ["oliveira", "morais", "laender"]
print(str_in_list(s, l))
s = "lenizio"
print(str_in_list(s, l))