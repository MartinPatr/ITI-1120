
n = int(input("How many words would you like to enter: "))
words = []

for i in range(0,n):
    words.append(input("Enter string: "))

final = input("Enter word youre trying to find: ")
for i in range(0,len(words)):
    for j in range(0,len(words[0])):
        if len(words[i]) == j+1:
            print(words[i][j])
        else:
            print(words[i][j],end=' ')

found = False
#Check horizontally first
for i in range(0,len(words)):
    if final in words[i]:
        x = words[i].rfind(final)
        print(final, "is at row" ,i, "and column",(x+1), "horizontally.")
        found == True
        break

#Check vertically
if found == False:
    for i in range(0,len(words)):
        if len(words)-i < len(final):
            break
        for j in range(0,len(words[i])):
            horizontal = 0
            if words[i][j] == final[0]:
                for x in range(1,len(final)):
                    if words[i+x][j] != final[x]:
                        pass
                    else:
                        horizontal = horizontal + 1
            if horizontal + 1 == len(final):
                print(final, "is at row" ,(i +1), "and column",(j+1), "vertically.")
                found = True
                break

#Check diagonally
if found == False:
    for i in range(0,len(words)):
        if len(words)-i < len(final):
            break
        for j in range(0,len(words[i])):
            diagonal_right = diagonal_left =0
            if words[i][j] == final[0]:
                for x in range(1,len(final)):
                    if words[i+x][j+x] != final[x]:
                        pass
                    else:
                        diagonal_right = diagonal_right + 1
                    if words[i+x][j-x] != final[x]:
                        pass
                    else:
                        diagonal_left = diagonal_left + 1
            if diagonal_right + 1 == len(final):
                print(final, "is at row" ,(i +1), "and column",(j+1), "diagonally.")
                found == True
                break
            if diagonal_left + 1 == len(final):
                print(final,"is at row",(i + 1),"and column",(j+1),"diagonally ")
                found == True
                break