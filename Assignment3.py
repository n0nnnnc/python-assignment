# First Product
first_product_name = str(input("Enter The 1st Product Name:"))
first_price = float(input("Enter Price of Product:"))
first_quantity = int(input("Enter Quantity of Product:"))

# Second Product
second_product_name = str(input("Enter The 2st Product Name:"))
second_price = float(input("Enter Price of Product:"))
second_quantity = int(input("Enter Quantity of Product:"))

# Third Product
third_product_name = str(input("Enter The 3nd Product Name:"))
third_price = float(input("Enter Price of Product:"))
third_quantity = int(input("Enter Quantity of Product:"))

print("-" * 50)
print("Inventory".center(50, " "))
print("-" * 50)
print("Item".center(30) + "Price".center(10) + "Quantity".center(10))
print("-" * 50)

print(
    first_product_name.ljust(30)
    + str(first_price).center(10)
    + str(first_quantity).rjust(10)
)
print(
    second_product_name.ljust(30)
    + str(second_price).center(10)
    + str(second_quantity).rjust(10)
)
print(
    third_product_name.ljust(30)
    + str(third_price).center(10)
    + str(third_quantity).rjust(10)
)
print("-" * 50)

total_quantity = "Total Quantity = " + str(
    first_quantity + second_quantity + third_quantity
)

print(total_quantity.rjust(50))
print("-" * 50)
