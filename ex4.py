def read_floats(n):
    return [input(f"Input value {x + 1} out of {n}: ") for x in range(n)]

print(read_floats(2))