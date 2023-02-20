import random
number_users = int(input("Please enter the amount of players: "))
max = int(input("Please enter the maximum integer: "))
players = []
scores = []
high_scores =[]

players.append(input("What is your name Player 1? "))
#This for loop will play the game for each player
for i in range(0,number_users):
        print("starting game for",players[i])
        round_number = 1
        c = -1
        x = random.randint(0, max)
        while c != x:
            c = int(input("Please enter your guess: "))
            if c > x:
                print("Too large")
                round_number = round_number + 1
            elif c < x:
                print("Too small")
                round_number = round_number + 1
            else:
                print("Congradulations you got it in:",round_number, "Guesses")
                print("The number was:", x )
                scores.append(round_number)
                if i == (number_users - 1):
                    break
                answer = input("Do you want to play again?: ")
                players.append(answer)

high_scores = scores.copy()
#This will find the lowest number of guesses and find which player it belonged to
high_scores.sort()
lowest_score = high_scores[0]
x = scores.index(lowest_score)
#This if statement will print to make sure our print statement matches the assigment output
if high_scores[1] == high_scores[0]:
    print(players[0], end =',')
    for j in range(1,len(high_scores)):
        if high_scores[j] == high_scores[0]:
            high_scores.append(-1)
            if high_scores[j+1] != high_scores[0]:
                print(players[j],end =' ')
            else:
                print(players[j],end =',')
    print("are winners")
else:
    print(players[x], "is the winner")
