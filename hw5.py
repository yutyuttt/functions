def remove(orig, x, out):
    count = 0
    for i in range(len(orig)):
        if orig[i] == x:
            count += 1
            continue

        out[i - count] = orig[i]

    for i in range(count):
        out[-(i + 1)] = 0

orig = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
x = 4
out = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
remove(orig, x, out)

print(out)    
    