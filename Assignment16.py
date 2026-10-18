from math import floor, pi, sqrt


def findAreaCircle(r):
    area_circle = round(pi * (r**2), 2)
    return area_circle


def findAreaSquare(l):
    area_square = l**2
    return area_square


def findAreaEquiTriangle(l):
    area_equi_triangle = round((sqrt(3) * (l**2)) / 4, 2)
    return area_equi_triangle


shape = []
dict = {
    "Circle": {i: findAreaCircle(i) for i in range(1, 101)},
    "Square": {i: findAreaSquare(i) for i in range(1, 101)},
    "Triangle": {i: findAreaEquiTriangle(i) for i in range(1, 101)},
}
# print(dict)
while True:
    shape = input(
        "Enter geometry shape for an area calculation\n[Circle, Square, Triangle]\n[Enter something else to exit this program]:"
    )
    shape = shape.capitalize()
    if shape in dict:
        key = float(input("Enter the dictionary key\n[1-100]:"))
        key = floor(key)
        if 1 <= key < 100:
            area = dict[shape][key]
            print("-" * 50)
            print("The area of {} is {}".format(shape.upper(), format(area)))
            print("-" * 50)
        else:
            print("!!! The key is out of scope !!!")
            print("")
            break
    else:
        print("")
        break
