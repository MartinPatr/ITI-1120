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




penalties = round = black = white = 0
round = 1
score = {
        "Round1": [],"Round2": [],"Round3": [],"Round4": [],"Round5": [],"Round6":[],
        "Round7": [],"Round8": [],"Round9": [],"Round10": [],"Round11":[],"Round12":[],
        "Round13":[],"Round14":[],"Round15":[]
    }

keys = list(score.keys())
guess1 = ["red", "yellow", "blue", "green"]
guess2 = [ "orange", "pink", "purple", "cyan"]
correct = { "position1":[guess1.copy()],"position2":[guess1.copy()],"position3":[guess1.copy()],"position4":[guess1.copy()]}

while round <= 15 and black < 4:
    First = False
    Equal = False
    completion1 = False
    #The Bot
    if round == 1:
        guesses  = guess1.copy()
    if round == 2:
        guesses  = guess2.copy()
    if round >= 3:
        total1 = score["Round1"]
        total2 = score["Round2"]
        print(total1)
        print(total2)
        if (total1[0]) + (total1[1]) > (total2[0]+(total2[1])):
            First = True
        elif (total1[0]) + (total1[1]) < (total2[0]+(total2[1])):
            pass
        else:
           Equal == True
        if First:  
            if black != (total1[0]) + (total1[1]):
                if round == 4:
                    pass
                guesses = guess1.copy()
            else:
                completion1 = True
        if First == False:
            if black != (total1[0]) + (total1[1]):
                random.shuffle(guess2)
                guesses = guess2.copy()
            else:
                completion1 = True

        





        
    black = white = 0
    for i in range (0,4):
        if selected_colors.count(guesses[i]) > 0:
            if selected_colors.index(guesses[i]) == i:
                black = black + 1
            else:
                white = white + 1
    print("White:",white)
    print("Black",black)
    score[keys[round-1]].append(white)
    score[keys[round-1]].append(black)
    round = round + 1
    print(guesses)
    print(score)
print("Congrats you won")
print(selected_colors)

print()
print(correct)