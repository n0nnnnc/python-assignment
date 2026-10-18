print("Making a list of Factorial series of n")
n = int(input("Enter 'n' of Factorial number:"))

factorial_list = []
factorial = 1
for i in range(1, n + 1):
    factorial *= i
    factorial_list.append(factorial)
# print(factorial_list)
print("A list of Factorial series of {} is {}".format(n, factorial_list))
print(" ")
