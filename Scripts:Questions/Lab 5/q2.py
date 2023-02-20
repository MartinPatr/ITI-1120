import statistics

def average(integers):
    sum = 0
    for i in range(0,len(integers)):
        sum = sum + integers[i]
    return sum/len(integers)


numbers = []
n = int(input("How many numbers do you want to check: "))
for i in range(0,n):
    numbers.append(float(input("Please enter a integer: ")))

print("The Standard deviation:",statistics.pstdev(numbers))