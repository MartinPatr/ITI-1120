import random
import string
#Real Functions given
def sumIntegers(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum

def sequence(n):
    seq = [ ]
    while n != 1:
        seq.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    seq.append(1)
    return seq

def check(word):
    n = len(word)
    i = 0
    j = n - 1
    while i < j:
        if word[i] != word[j]:
            return False
        i = i + 1
        j = j - 1
    return True

#My recursive functions
def rec_sumIntegers(n):  
    if n == 0:
        return 0
    return rec_sumIntegers(n-1) + n

def rec_sequence(n):
    list1 = [n]
    if n == 1 :
        return [1]      
    if n % 2 == 0 :
        list1.extend(rec_sequence(n//2))     
    else:
        list1.extend(rec_sequence(n*3+1))    
    return list1

def rec_check(word):
    if len(word) <= 1:
        return True
    if word[0] == word[-1]:
        return rec_check(word[1:-1])
    else:
        return False

#Check if recursive functions work
print('Checking sumIntegers function')
for i in range(1,9):
    if sumIntegers(i) != rec_sumIntegers(i):
        print("Failed Test:",i)
    else:
        print("Passed Test:",i)
print()
print('Checking sequence function')
for i in range(1,4):
     if sequence(i) != rec_sequence(i):
         print("Failed Test:",i)
     else:
         print("Passed Test:",i)
print()
print("Checking random word sequence")
for i in range(0,4):
    random_word = (''.join(random.choices(string.ascii_lowercase, k=5)))
    if check(random_word) != rec_check(random_word):
        print("Failed Test:",i)
    else:
        print("Passed Test:",i)
