import random
a = int(input("Please enter an integer larger than 1: "))

divisors = []
primes = []

#This for loop will find the divisors for that number
for i in range(2,a + 1):
    if a % i == 0:
        divisors.append(i)

#Then check the primes of the divisors
for j in range(0, len(divisors)):
    k = divisors[j]
    is_prime = True
    for x in range(2,k):
        if k % x == 0:
            is_prime = False
    if is_prime:
        primes.append(k)

max = 15
p1 = p2 = p3 = p4 = 0
#Check all possible combinations with to see if we require some numbers to be powerd
if len(primes) == 2:  
    while sum != a:
        p1 = random.randint(1, max)
        p2 = random.randint(1, max)
        sum = (primes[0]**p1) * (primes[1]**p2)
    print(a," = ",primes[0],end = "",sep='')
    if p1 > 1: print("^",p1,end ='',sep='') 
    print(" * ",primes[1],end ='',sep='')
    if p2 > 2: print("^",p2, end = '',sep='')
elif len(primes) == 3:
    while sum != a:
        p1 = random.randint(1, max)
        p2 = random.randint(1, max)
        p3 = random.randint(1, max)
        sum = (primes[0]**p1) * (primes[1]**p2) * (primes[2]**p3)
    print(a," = ",primes[0],end = "")
    if p1 > 1: print("^",p1,end='',sep='') 
    print(" * ",primes[1],end ='',sep='')
    if p2 > 1: print("^",p2,end='',sep='')
    print(" * ",primes[2],sep='', end="")
    if p3 > 1: print("^",p3,end='',sep='')
elif len(primes) == 4:
    while sum != a:
        p1 = random.randint(1, max)
        p2 = random.randint(1, max)
        p3 = random.randint(1, max)
        p4 = random.randint(1, max)
        sum = (primes[0]**p1) * (primes[1]**p2) * (primes[2]**p3) * (primes[3]**p4)
    print(a," = ",primes[0],end = "")
    if p1 > 1: print("^",p1,end='',sep='') 
    print(" * ",primes[1],end ='',sep='')
    if p2 > 1: print("^",p2,end='',sep='')
    print(" * ",primes[2],end='',sep='')
    if p3 > 1: print("^",p3,end='',sep='')
    print(" * ",primes[3],end='',sep='',)
    if p4 > 1: print("^",p4,end='',sep='')
else:
    while sum != a:
        p1 = random.randint(1, max)
        sum = (primes[0]**p1)
    print(a," = ",primes[0],end='',sep='')
    if p1 > 1: print("^",p1,sep='')
print("")
