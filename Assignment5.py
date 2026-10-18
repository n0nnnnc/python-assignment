strA = input("Please enter the string A :")
strB = input("Please enter the string B :")

print("-" * 40)

setA = set(strA)
setB = set(strB)
# print(setA)
# print(setB)

print("A number of character in A is {}".format(len(setA)))
print("A number of character in B is {}".format(len(setB)))

AB = setA & setB
# print(AB)
# print(len(AB))
print("A number of character in both A and B is {}".format(len(AB)))

# A_minus_B = setA.difference(setB)
A_minus_B = setA - setB
# B_minus_A = setB.difference(setA)
B_minus_A = setB - setA
print("Characters in A but not in B is {}".format(A_minus_B))
print("Characters in B but not in A is {}".format(B_minus_A))

# AB_sys_diff = setA.symmetric_difference(setB)
AB_sys_diff = setA ^ setB
print("Characters in A or B but not in both A and B is {}".format(AB_sys_diff))

# A_union_B = setA.union(setB)
A_union_B = setA | setB
print("All Characters in A or B is {}".format(A_union_B))
