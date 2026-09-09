def abs_value(x):
    if x < 0:
        return -x
    else:
        return x

print(abs_value(-1))

def distance(a, b):
    return abs_value(a - b)

print(distance(-1, 5))