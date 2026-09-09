def alternate(lst):
    res = []
    for i in range(len(lst) // 2):
        res.append(lst[i])
        res.append(lst[-(i + 1)])

    return res

a = [1, 2, 3, 4, 5]
print(alternate(a))