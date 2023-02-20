import random
while True:
    a = int(input("Please enter the first integer: "))
    b = int(input("Please enter the second integer: "))
    round_number = 1
    c = 1
    x = random.randint(a, b)
    while c != x:
        c = int(input("Please enter your guess: "))
        if c > x:
            print("Too large")
            round_number = round_number + 1
        elif c < x:
            print("Too small")
            round_number = round_number + 1
        else:
            print("Congradulations you got it in:",end = " ")
            print(round_number, end = " ")
            print("Guesses")
            print("The number was:", x )
            answer = input("Do you want to play again[y/n]: ")
            if answer != "y":
                break
            
