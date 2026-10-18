values = [10, 9, 5, 4, 1]
syms = ["X", "IX", "V", "IV", "I"]
roman_dict = {}


def numToRoman(num):
    roman = ""
    i = 0
    while num > 0:
        for _ in range(num // values[i]):
            roman += syms[i]
            num -= values[i]
        i += 1
    return roman


roman_dict = {i: numToRoman(i) for i in range(40)}
# print(roman_dict)

input_num = int(input("Enter a number for roman number conversion:"))
while 1 <= input_num <= 39:
    print('The roman number of {} is " {} "'.format(input_num, roman_dict[input_num]))
    input_num = int(input("Enter a number for roman number conversion:"))
print(" ")
