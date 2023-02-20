import math

a = int(input("Enter First Cofficient: "))
b = int(input("Enter Second Cofficient: "))
c = int(input("Enter Third Cofficient: "))

des =((b*b) - 4 * a * c)

if des < 0:
    print("There are zero roots in this function!")
elif des == 0:
    print("There is one root")
    print(f"Root:{-b/(2 * a)}")
elif des > 0:
    print("there are two roots")
    print(f"Root 1:{(-b+math.sqrt(des))/(2*a)}")
    print(f"Root 2:{(-b-math.sqrt(des))/(2*a)}")