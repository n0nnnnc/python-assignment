# 1) รหัสลับจะต้องมีอักษรภาษาอังกฤษตัวพิมพ์ใหญ่อย่างน้อย 1 ตัวอักษร (A-Z)
# 2) รหัสลับจะต้องมีอักษรภาษาอังกฤษตัวพิมพ์เล็กอย่างน้อย 1 ตัวอักษร (a-z)
# 3) รหัสลับจะต้องมีตัวเลข (0-9) อย่างน้อย 1 ตัวเลข
# 4) รหัสลับจะต้องมีความยาวไม่น้อย 8 ตัวอักษร (หรือตัวเลข)
# 5) รหัสลับจะต้องมีความยาวไม่เกิน 16 ตัวอักษร (หรือตัวเลข)
password = input("Setting your password:")
has_upper = False
has_lower = False
has_numeric = False

for letter in password:
    if letter.isupper() == True:
        has_upper = True
        break
for letter in password:
    if letter.islower() == True:
        has_lower = True
        break
for letter in password:
    if letter.isnumeric() == True:
        has_numeric = True
        break

while True:
    if has_upper == False:
        print("!!!ERROR!!! The password must contain at least a capital letter")
        print(" ")
        break
    if has_lower == False:
        print("!!!ERROR!!! The password must contain at least a lowercase letter")
        print(" ")
        break
    if has_numeric == False:
        print("!!!ERROR!!! The password must contain at least a number")
        print(" ")
        break
    if len(password) < 8:
        print("!!!ERROR!!! The password must contain at least 8 characters")
        print(" ")
        break
    if len(password) > 16:
        print("!!!ERROR!!! The password must not contain more than 16 characters")
        print(" ")
        break
    print(":-) Your password is correct (-:")
    print(" ")
    break
