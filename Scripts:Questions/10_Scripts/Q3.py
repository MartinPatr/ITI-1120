import math

x = float(input("Enter angle number: "))
n = int(input("Enter the number of terms in the series: "))

sin = x
cos = 1
c = 1
#Loop doing formula given
for i in range(2,n + 3,2):
    if c%2==0:
        multi = 1
    else:
        multi = -1
    sin = sin + ((x**(i + 1))/(math.factorial(i + 1)) * multi)
    cos = cos + ((x**i)/(math.factorial(i)) * multi)
    c += 1

#Print Statementss
print(f"Sin({x}) =",end=' ')
print(f"{sin:.9f}")
print(f"Cos({x}) =",end=" ")
print(f"{cos:.9f}")