m = int(input("Enter the x coefficient"))
y_int = int(input("Enter y intercept"))
x = int(input("Enter x coordinate"))
y = int(input("Enter y coordinate"))

if y < y_int:
    if m > 0:
        print("Its on the right of the line")
    elif m < 0:
        print("Its on the left of the line")
elif y > y_int:
    if m > 0:
        print("Its on the left of the line")
    elif m < 0:
        print("Its on the right of the line")
else:
    if x != 0:
        if m > 0 and x > 0:
            print("Its on the right of the line")
        elif m < 0 and x < 0:
            print("Its on the left of the line")
        elif m > 0 and x < 0:
            print("its on the left of the line")
        else:
            print("its on the right of the line")