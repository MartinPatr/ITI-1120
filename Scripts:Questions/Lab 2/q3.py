n = int(input("Enter a non-negative integer: "))
int = n
digit_count = 0
#While the number does not = 0 it will keep dividing the number by 10 
#And for each division it will add one to the counter
while n != 0:
    n = n//10
    digit_count = digit_count + 1

integers = []
#This for loop will get the amount of digits and get it to a divisible by 100,1000,etc
d = 1
for i in range (1,digit_count):
    d = d * 10

#This for loop will grab each digit and add it to a list from the total integer
c = d
for i in range(1,digit_count + 1):
    integers.append(((int/d)%10))
    d = d/10

#This for loop will add the each digit and multiply by each 100,10m,etc
total = 0
for y in range(1,digit_count + 1):
    total = total + (integers[len(integers)-y]*c)
    c = c/10


print("The reversed integer is:", total)
