def read_ints() -> list:
    ints = []
    while (val := input("Enter an integer: ")) != "":
        ints.append(int(val))

    return ints

print(read_ints())