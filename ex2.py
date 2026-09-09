def interleave(a, b):
    res = []
    for (x, y) in zip(a, b):
        res.append(x)
        res.append(y)

    return res

a = [5, 2, 3]
n = [4, 7, 6]
print(interleave(a, n))