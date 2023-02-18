a = int(input("Enter first integer:"))
b =int(input("Enter second integer:"))

primes = []

#It will check each i in range of integers a and b
for i in range(a,b):
    #After each for loop of each individual number it will assume the next number is a prime
    is_prime = True
    #This for loop will check every number in between 2 and and the number that we are checking
    for j in range(2,i-1):
        #if the number(i) that we are checking can be  divided by the numbers we are increasing
        #Then we set is_prime to false allowing it not to be added to the prime numbers list
        if i % j == 0:
            is_prime = False
    if is_prime:
        primes.append(i)

print(primes)
print("Number of primes:", len(primes))