import random

colors = ["red", "yellow", "blue", "green", "orange", "pink", "purple", "cyan", "silver", "teal"]
temp_colors = colors.copy()
selected_colors = []
count = 0
#Getting the 4 selected colors
for i in range(0,4):
    color_selected = random.randint(0,9-count)
    selected_colors.append(temp_colors[color_selected])
    temp_colors.pop(color_selected)
    count = count + 1

#print(selected_colors)
#Print statements introducing the player to the game
user_name = input("What is your name? ")
print('Welcome to Master Mind',user_name + "!")
print("The code maker is here. Available colors are")
print("Red, Yellow, Blue, Green, Orange, Pink, Purple, Cyan, Silver, Teal")
print("You have 15 guesses, total of 5 penalties are allowed but avoid penalties.")
print("The code maker selected 4 colors.")
print("You can start guessing",user_name + ".")


penalties = round = black = white = 0
round = 1

#While loop to play the rounds
while round <= 15 and black < 4 and penalties < 5:
    guesses = input("Enter guess " + str(round) + ": ").lower()
    guesses = guesses.split()
    Penalty = False
    checker = [False,False,False]
    #First penalty check if correct amount of colors were typed in
    if len(guesses) != 4:
        Penalty = checker[0] = True
        
    #Penalty check if they entered a real color
    for elem in guesses:
        if colors.count(elem) == 0 and Penalty == False:
            Penalty = checker[1] = True
    
    #Penalty to check if they enetered repeated colors
    for elem in guesses:
        if guesses.count(elem) > 1:
            print("Sorry",user_name + ',', "repeated colors are not allowed in this game.",end = " ")
            if checker[0] == True:
                print("Also, cannot recognize the colors you entered.",end = "")
            if checker[1] == True:
                print("Also, you need to enter at least 4 colors for each guess.",end ="")
            print(" One penalty is considered.")
            Penalty = checker[2] = True
            break
    #Penalty print statement
    if checker[1] == True and checker[2] == False:
        print("Sorry", user_name + ",", "cannot recognize the colors you entered. ",end='')
        if checker[0] == True:
            print("Also, you need to enter at least 4 colors for each guess.",end = " ")
        print(" One penalty will be applied")
        Penalty = checker[1] = True
        
    #Penalty print statement
    if checker[0] == True and checker[2] == False and checker[1] == False:
        print("Sorry",user_name +",", "you need to enter at least 4 colors for each guess. One penalty is considered.")
        Penalty = checker[0] = True

    if Penalty:
        penalties = penalties + 1
        print("Total penalties = ",penalties)
        
    
    #Checking how many whites and how many blacks
    black = white = 0
    if Penalty != True:
        for i in range (0,4):
            if selected_colors.count(guesses[i]) > 0:
                if selected_colors.index(guesses[i]) == i:
                    black = black + 1
                else:
                    white = white + 1
    round = round + 1
    #Print statements for how many white and black
    if Penalty != True:
        print("You got",black,end =" ")
        if black > 1:
            print("blacks",end=",")
        else:
            print("black",end=",")
        print(" and",white,end =' ')
        if white > 1:
            print("whites",end ="")
        else:
            print("white", end ='')
        print(" for this guess.")
        
#Final Print statements
if black == 4:
    print("You won the game with", (round - 1), "guesses and", penalties, "penalties, Congratulations.")
if round > 15:
    print("Sorry",user_name + ",","you ran out of guesses and you lost the game with 2 penalties.")
if penalties == 5:
    print(user_name + ",","you lost the game by reaching the maximum number of allowed penalties.")