
n = int(input("Please enter the amount of lines you want for the triangle: "))

#For loop to create each row
for i in range(0,n):
    r = 1
    #For loop adding each number of the traingle
    round_count = 0
    for x in range(0, i + 1):
        #If statement to make only the first number(1) is printed without a space in the beggening
        if round_count == 0:
            print(r,end = "")
        else:
            print(" ",r,end = "")
        round_count = round_count + 1

    print()