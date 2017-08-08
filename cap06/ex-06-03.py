listax = [1,2,3,4,5,8]
listay = [4,5,6,7,8]
listaz = []
listax.extend(listay)
x = 0
while x < len(listax):
    y = 0
    while y < len(listaz):
        if listax[x] == listax[y]:
            break
        y += 1
    if y == len(listaz):
        listaz.append(listax[x])
    x = x + 1

print(listaz)