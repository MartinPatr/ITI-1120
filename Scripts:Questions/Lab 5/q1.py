def sum(integer):
    divisors = []
    for i in range(1,integer):
        if integer % i == 0:
            divisors.append(i)
    
    sum = 0
    for i in range(0,len(divisors)):
        sum = sum + divisors[i]
    return sum

numbers = []
n = int(input("what number do you want to check: "))
if sum(n) == n:
    print(n,"is a complete number.")
else:
    print(n,"is a not complete number.")
