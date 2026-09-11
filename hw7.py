# 1
def iterate(f, x, n):
    res = []
    val = x
    for _ in range(n):
        val = f(val)
        res.append(val)
    return res

def f(x):
    return 0.5 * (x + 2 / x)

print(iterate(f, 1, 6))

# 2
def apply_functions(fs, x):
    val = x
    for i in range(len(fs)):
        val = fs[-(i + 1)](val)
    return val

fs = ["...".join, str.split, str.lower]
x = "WHAT IS THIS?"
print(apply_functions(fs, x))