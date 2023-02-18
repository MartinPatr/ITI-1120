n = int(input("Please enter the amount of integers you want to enter: "))

numbers = []
#This for loop will get all the integers that we will need to check
for i in range(1,n + 1):
    x = int(input("Please enter the integer: "))
    numbers.append(x)

#For loop checking each number in number array
for j in range(0,len(numbers)-1):
    round_counter = 0
    temp = numbers[j]
    #This will get rid of the current number we are checking from the list
    numbers.pop(j)
    for x in range(0,len(numbers)):
        if temp == numbers[x]:
            break
        round_counter = round_counter + 1
    #If the number went through each other integer without breaking, then it is individual
    if round_counter == len(numbers):
        indv_integer = temp
        break
    numbers.insert(j,temp)
    

print("The individual number is",indv_integer)

