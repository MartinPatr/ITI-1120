import math
eq1 = []
eq2 = []
eq3 = []

eq4 = []
eq5 = []

eq6 = []
#This for loop will get all the integers that we will need to check
for i in range(1,13):
     if i < 5:
         eq1.append(float(input("Please enter the coefficients for the first equation: ")))
     elif 9 > i >= 5:
         eq2.append(float(input("Please enter the coefficients for the second equation: ")))
     else:
         eq3.append(float(input("Please enter the coefficients for the third equation: ")))

#Set x variables
multi1 = multi2 = multi3 = 0
x1 = eq1[0]
x2 = eq2[0]
x3 = eq3[0]

#While loop to find mutliplier to find equation 4
while True:
    x1 = eq1[0]
    #Check if the mutliplier is positive
    if int(x1*multi1*100 - x2*100) == 0:
        break
    #Check if the multiplier is negative
    if int(x1*multi1*-1*100 - x2*100) == 0:
        break
    multi1 = multi1 + 0.01
multi1 = round(multi1+0.01, 2)


#While loop to find mutliplier to find equation 4
while True:
    x2 = eq2[0]
    #Check if the mutlipliar is positive
    if int(x2*multi2*100 - x3*100) == 0:
        break
    #Check if the multipliar is negative
    if int(x2*(multi2*-1)*100 - x3*100) == 0:
        break
    multi2 = multi2 + 0.01
multi2 = round(multi2+0.01,2)


eq1 = [x1 * multi1 for x1 in eq1]
for j1 in range(0,4):
    eq4.append(eq1[j1] - eq2[j1])
    eq4[j1] = round(eq4[j1],2)

eq2 = [x2 * multi2 for x2 in eq2]
for j2 in range(0,4):
    eq5.append(eq2[j2] - eq3[j2])
    eq5[j2] = round(eq5[j2],2)

print(eq4)
print(eq5)

y1 = eq4[1]
y2 = eq5[1]
#While loop to find mutliplier to find equation 4
while True:
    y1 = eq4[1]
    #Check if the mutliplier is positive
    if int(y1*multi3*100 - y2*100) == 0:
        break
    #Check if the multiplier is negative
    if int(y1*(multi3*-1)*100 - y2*100) == 0:
        break
    multi3 = multi3 + 0.01
multi3 = round(multi3+0.01,2)

eq4 = [y1 * multi3 for y1 in eq4]
for j3 in range(0,4):
    eq6.append(eq4[j3] - eq5[j3])
    eq6[j3] = round(eq6[j3],2)

print(eq6)
z = eq6[4]/eq6[2]
print(z)