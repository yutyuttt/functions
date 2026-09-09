# global vars
g = -1
y = -2
x = -3
def f(x):
    def h(y):
        # y bound locally, x in enclosing, g globally
        print(f'g={g}, y={y}, x={x}')
    return h # returns function

func = f(1)
func(2)