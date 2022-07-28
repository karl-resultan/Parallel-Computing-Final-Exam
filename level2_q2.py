side1 = int(input("Please enter the first side: "))
side2 = int(input("Please enter the second side: "))
side3 = int(input("Please enter the third side: "))

if (side1**2 + side2**2) == (side3**2):
    print("This is a right triangle.")
else:
    print("This is not a right triangle.")