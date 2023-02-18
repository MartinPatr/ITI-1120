n = int(input("Please enter how many integers you want to check: "))
k = int(input("Please enter what integer you want the n interges to start with: "))

#While loop finding the amount of digits for k
temp = k 
digit_k = 0
while temp != 0:
    temp = temp//10
    digit_k = digit_k + 1

return_integers = []
#For loop going through the process of asking and checking for each integer
for i in range(1,n + 1):
    x = int(input("Please enter a integer: "))
    temp = temp_digits = x
    #While loop finding amount of digits for this integer
    digit_x = 0
    while temp_digits != 0:
        temp_digits = temp_digits//10
        digit_x = digit_x + 1
    #Here you will get the amount of digits you need to divide
    div = 10**(digit_x - digit_k)
    #Here you will get rid of all digits other than the k amount in the beggening
    r = x%div
    x = x - r
    #If statement will check if the first amount of digits of the interger match k, if yes add to list
    if (x//div) == k:
        return_integers.append(temp)

print(*return_integers)