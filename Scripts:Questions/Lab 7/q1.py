setU = set()
setA = set()
setB = set()
#This will get our inputs
n = int(input("Please enter the amount of integers for set A: "))
for i in range(0,n):
    setU.add(input("Enter integer: "))
n = int(input("Please enter the amount of integers for set B: "))
for i in range(0,n):
    setA.add(input("Enter integer: "))
n = int(input("Please enter the amount of integers for set C: "))
for i in range(0,n):    
    setB.add(input("Enter integer: "))

#A union B
AunionB = setA.union(setB)

#A intersection B 
AintersectionB = setA.intersection(setB)

#Set A minus Set B
AminusB = setA - setB

#Set B minus Set A
BminusA = setB - setA


#A-Complement
Acomplement = setU - setA

#B-Complement
Bcomplement = setU - setB

#ApowerB
ApowerB = AminusB.union(BminusA)

#print statments
print("A Union B = ",AunionB)
print("A intersection B =",AintersectionB)
print("A-B",AminusB)
print("B-A",BminusA)
print("A Complement =",Acomplement)
print("B Complement =",Bcomplement)
print("A power B=",ApowerB)
if setA.union(setB) == setB:
    print("A is a subset of B",end =", ")
else:
    print("A is not a subset of B",end =", ")

if setB.union(setA) == setA:
    print("and B is a subset of A")
else:
    print("and B is not a subset of A")