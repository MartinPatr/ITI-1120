n = int(input("Enter a non-negative integer: "))
print(n, end=',')
while n != 1:
    if n%2 == 0:
        n = n/2
    else:
        n = n*3 + 1
    print(int(n), end = ',')
