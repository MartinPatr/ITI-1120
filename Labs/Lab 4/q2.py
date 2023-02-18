n = int(input("Please enter the amount of integers you want to enter: "))

numbers = []
differences = []
#This for loop will get all the integers that we will need to check
for i in range(1,n + 1):
    numbers.append(float(input("Please enter the integer: ")))
numbers=sorted(numbers)

#This for loop will get all the differenes
for j in range(len(numbers)-1,0,-1):
    difference = float((numbers[j]-numbers[j-1]))
    differences.insert(0,difference)

#This will create a copy of the differences and then sort it
differences_copy = differences.copy()
differences_copy=sorted(differences_copy)

#This will get the the position of what numbers have the lowest difference
x = differences.index(differences_copy[0])


print(numbers[x], numbers[x+1])

