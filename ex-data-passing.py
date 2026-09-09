def f(lst, x):
    x *= 5
    lst.append(x)

lst = list(range(5))
x = 11
f(lst, x)
print(lst, x)