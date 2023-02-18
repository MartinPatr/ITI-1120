a = input("Enter First Digit: ")
b = input("Enter Second Digit: ")
c = input("Enter Third Digit: ")

if a >= b and a >= c:
    if b >= c:
        print("Largest", a + b + c)
        if c == 0:
            print("Smallest", int(b + a))
        else:
            print("Smallest", int(c + b + a))
    else:
        print("Largest", a + c+ b)
        if b == 0:
            print("Smallest", int(a + c))
        else:
            print("Smallest",int(b + a + c))

if b >= a and b >= c:
    print(b, "Is the maximum")
    if a > c:
        print("Largest", b + a + c)
        if c == 0:
            print("Smallest", int(a + b))
        else:
            print("Smallest", int(c + a + b))
    else:
        print("Largest", b + c + a)
        if a == 0:
            print("Smallest", int(a + c + b))
        else:
            print("Smallest",int(a + c + b))
if c >= a and c >= b:
    if a > b:
        print("Largest", c + a + b)
        if b == 0:
            print("Smallest",int(a + c))
        else:
            print("Smallest",int(b + a + c))
    else:
        print("Largest", c + b + a)
        if a==0:
            print("Smallest",b + c)
        else:
            print("Smallest",int(a + b + c))