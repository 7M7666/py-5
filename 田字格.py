def print_field(rows, cols):
   
    for _ in range(cols):
        print("+----", end="")
    print("+")
    for _ in range(rows):
        for _ in range(cols):
            print("|    ", end="")
        print("|")
        for _ in range(cols):
            print("+----", end="")
        print("+")

print_field(3, 3)
