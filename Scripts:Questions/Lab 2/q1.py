n = int(input("Please enter a positive integer:"))
divisors = []
#For loop to check if each number in between 1 and input is divisable if so add to list divisors
for i in range(1,n + 1):
    if n%i == 0:
        divisors.append(i)

#For loop to print each integer from divisors 
#Then use a if statement to check if its last to make sure not to print extra ,
print("Divisors: ", end ='')
for x in range(len(divisors)):
    if x == len(divisors) - 1:
        print(divisors[x],)
    else:
        print(divisors[x], end=',')
#Print the sum of alll divisors using sum()
print("Sum of Divisors:", sum(divisors))
