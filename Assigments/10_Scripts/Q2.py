n = int(input("Please enter the integer you wish to convert: "))
b = int(input("Please enter the base you want to convert to: "))

r = []

#Keep dividing and getting the remainder
while n > 0:
    r.append(str(n%b))
    n = n//b

#Reverse and add them together as strings giving you the final result
r.reverse()
print(''.join(r))