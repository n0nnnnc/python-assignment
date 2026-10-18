print("-" * 9 + " " + 'Drawing the square rectangular by "#"' + " " + "-" * 9)
print('[To quit this program by pressing "0"]')
print("-" * 57)

size = int(input("Please enter the size:"))
while size != 0:
    for i in range(size):
        if i == 0 or i == size - 1:
            print("#" * size)
        else:
            print("#" + " " * (size - 2) + "#")
    size = int(input("Please enter the size:"))
    if size == 0:
        print(" ")
        break
