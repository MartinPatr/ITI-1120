from statistics import mode
n = int(input("How many integers would you like to check for: "))

numbers = []
#This for loop will get all the integers that we will need to check
for i in range(1,n + 1):
    x = float(input("Please enter the integer: "))
    numbers.append(x)

numbers.sort()
#This will do each calculation to reach each goal
print("Average =",(sum(numbers)/len(numbers)))
print("Modes =",mode(numbers))
if len(numbers) % 2 == 0:
    half = len(numbers)//2
    print("Median =",(numbers[half]+numbers[half-1])/2)
else:
    half = len(numbers)//2
    print("Median =",numbers[half])
print("Range =",numbers[-1]-numbers[0])