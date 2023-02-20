a = int(input("Enter first integer:"))
q = int(input("Enter second integer:"))
n = int(input("Enter third integer:"))

integers = []

integers.append(a)
#For loop starts that multiplies the first integer by the multipliar and adds it to the list
for i in range(1,n):
    a = a * q
    integers.append(a)

#For loop to print each integer from integers 
#Then use a if statement to check if its last to make sure not to print extra ,
for x in range(len(integers)):
    if x == len(integers) - 1:
        print(integers[x])
    else:
        print(integers[x], end=',')