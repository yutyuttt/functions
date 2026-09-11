# only works for odd length lists
def alternate(lst):
    res = []
    for i in range(len(lst) // 2):
        res.append(lst[i])
        res.append(lst[-(i + 1)])

    return res

a = [1, 2, 3, 4, 5]
print(alternate(a))

# takes into account both even and odd length lists
def alternate2(lst):
    res = []
    beg = 0
    end = len(lst) - 1
    for i in range(len(lst)):
        if i % 2 == 0:
            res.append(lst[beg])
            beg += 1
        else:
            res.append(lst[end])
            end -= 1

    return res