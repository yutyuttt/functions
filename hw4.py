# 1
def share(a, b):
    for item in a:
        if item in b:
            return True

    return False

# 2
print(share([1, 2, 3], [4, 5, 6]))
print(share([1, 2, 3], [4, 2, 6]))