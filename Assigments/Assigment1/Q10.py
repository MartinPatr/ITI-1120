#Input statements
n = int(input("Please enter the number of rows: "))
m = int(input("Please enter the number of columns: "))

#Formulaes used to find amount of squares and rectangles in each grid
r1 = n + 1
r2 = m + 1
rectangles = (m * n * r1 * r2) / 4
s1 = 2*m+1
squares = (m * r2 * s1/6) + (n-m) * m * (r2/2 )

#Print statements
print("Total number of rectangles =",int(rectangles))
print("Rectangles but not squares =",int(rectangles-squares))