g = 100 # global

def f(x):
    y = 20 # local
    return g + x + y

print(f(3))
try:
    print(x, y) # x, y not in scope
except NameError:
    print("name error")