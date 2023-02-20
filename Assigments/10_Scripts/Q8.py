setU = []
setA = []
setB = []
#This will get our inputs
n = int(input("Please enter the amount of integers for set A: "))
for i in range(0,n):
    setU.append(input("Enter integer: "))
n = int(input("Please enter the amount of integers for set B: "))
for i in range(0,n):
    setA.append(input("Enter integer: "))
n = int(input("Please enter the amount of integers for set C: "))
for i in range(0,n):    
    setB.append(input("Enter integer: "))
#Using dictionarys we will get rid of all duplicates
setU = list(dict.fromkeys(setU))
setA = list(dict.fromkeys(setA))
setB = list(dict.fromkeys(setB))
setU = list(set(setU))
setA = list(set(setA))
setB = list(set(setB))

#A union B
AunionB = setA + setB
AunionB = list(dict.fromkeys(AunionB))
AunionB.sort()

#A intersection B and A power B as they are opposites
AintersectionB = []
ApowerB = []
for i in range(0,len(AunionB)):
    intersection1 = False 
    intersection2 = False
    for j in range(0,len(setA)):
        if AunionB[i] == setA[j]:
            intersection1 = True
            break
    for x in range(0,len(setB)):
        if AunionB[i] == setB[x]:
            intersection2 = True
            break
    if intersection1 == True and intersection2 == True:
        AintersectionB.append(AunionB[i])
    else:
        ApowerB.append(AunionB[i])
        

#Set A minus Set B
AminusB = []
for i in range(0,len(setA)):
    round_count = 0
    for j in range(0,len(setB)):
        if setA[i] == setB[j]:
            break
        round_count = round_count + 1
    if round_count == len(setB):
        AminusB.append(setA[i])

#Set B minus Set A
BminusA = []
for i in range(0,len(setB)):
    round_count = 0
    for j in range(0,len(setA)):
        if setB[i] == setA[j]:
            break
        round_count = round_count + 1
    if round_count == len(setA):
        BminusA.append(setB[i])


#A-Complement
Acomp = []
for i in range(0,len(setU)):
    round_count = 0
    for j in range(0,len(setA)):
        if setU[i] == setA[j]:
            break
        round_count = round_count + 1
    if round_count == len(setA):
        Acomp.append(setU[i])

#B-Complement
Bcomp = []
for i in range(0,len(setU)):
    round_count = 0
    for j in range(0,len(setB)):
        if setU[i] == setB[j]:
            break
        round_count = round_count + 1
    if round_count == len(setB):
        Bcomp.append(setU[i])


AunionB.sort()
AintersectionB.sort()
AminusB.sort()
BminusA.sort()
Acomp.sort()
Bcomp.sort()
ApowerB.sort()

#print statments
print("A Union B = {",end ="")
for i in range(0,len(AunionB)):
    if AunionB[i] == AunionB[-1]:
        print(AunionB[i],end='')
    else:
        print(AunionB[i],end=',')
print("}")

print("A Intersection B = {",end ="")
for i in range(0,len(AintersectionB)):
    if AintersectionB[i] == AintersectionB[-1]:
        print(AunionB[i],end='')
    else:
        print(AunionB[i],end=',')
print("}")

print("A - B = {",end ="")
for i in range(0,len(AminusB)):
    if AminusB[i] == AminusB[-1]:
        print(AminusB[i],end='')
    else:
        print(AminusB[i],end=',')
print("}")

print("B - A = {",end ="")
for i in range(0,len(BminusA)):
    if BminusA[i] == BminusA[-1]:
        print(BminusA[i],end='')
    else:   
        print(BminusA[i],end=',')
print("}")

print("A Complement = {",end ="")
for i in range(0,len(Acomp)):
    if Acomp[i] == Acomp[-1]:
        print(Acomp[i],end='')
    else:   
        print(Acomp[i],end=',')
print("}")

print("B Complement = {",end ="")
for i in range(0,len(Bcomp)):
    if Bcomp[i] == Bcomp[-1]:
        print(Bcomp[i],end='')
    else:   
        print(Bcomp[i],end=',')
print("}")

print("A^B = {",end ="")
for i in range(0,len(ApowerB)):
    if ApowerB[i] == ApowerB[-1]:
        print(ApowerB[i],end='')
    else:   
        print(ApowerB[i],end=',')
print("}")