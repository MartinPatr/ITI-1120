str1 = str(input("Please enter a string: "))
str2 = str(input("Please enter the string you want to check: "))

positions = []
reverse_str1 = str1[::-1]
for i in range(0,len(str2)):
    round_count = 1
    #To check if the original integer is in the second string
    if str1[0] == str2[i]:
        for j in range(1,len(str1)):
            if len(str2) < i + round_count + 1:
                round_count = round_count - 1
            if str1[j] != str2[i + round_count]:
                break
            round_count = round_count + 1
        if len(str1) == round_count:
            positions.append(i)
    
    #To check if the reverse integer is in the second string
    round_count = 1
    if reverse_str1[0] == str2[i]:
        for j in range(1,len(reverse_str1)):
            if len(str2) < i + round_count + 1:
                round_count = round_count - 1
            if reverse_str1[j] != str2[i + round_count]:
                break
            round_count = round_count + 1
    if len(reverse_str1) == round_count:
        positions.append(((i + (len(reverse_str1)-1)) * -1))

#For loops to help make output the same as assigment requirement
duplicates = False
for x in range(0,len(positions)):
    for p in range(0,len(positions)):
        if positions[x] == positions[p] * -1:
            duplicates = True
            break
if duplicates == True:
    for x in range(0,len(positions)):
        for p in range(0,len(positions)):
            if positions[x] == positions[p] * -1:
                placement1 = positions.index(positions[p])
                placement2 = positions.index(positions[x])
                negative = positions[placement1]
                positions.pop(placement1)
                positions.insert(placement2,negative)
    positives = []       
    for x in range(0,len(positions)):
        round_count = 0
        for p in range(0,len(positions)):   
            if positions[x] != positions[p]*-1 and (positions[x]*-1) < 0:
                round_count = round_count + 1
        if round_count == len(positions):
            positives.append(positions[x])

    if len(positives) > 0:
        round_count = 0
        for x in range(0,len(positives)):
            placement3 = positions.index(positives[x])
            positions.pop(placement3)
            positions.insert(1+round_count,positives[x])
            round_count = round_count + 1


if len(positions) == 0:
    print('The string is not found in the string')
else:
    print(positions)


