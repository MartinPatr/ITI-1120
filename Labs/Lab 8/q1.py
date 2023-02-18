def upper_checker(matrix):
    upper = True
    for i in range(0,len(matrix[0])):
        row = matrix[i]
        for j in range(i+1,len(row)):
            if i == (len(matrix) - 1) and j == (len(row) - 1):
                break
            if row[j] != 0:
                upper = False
    return upper

def bottom_checker(matrix):
    bottom = True
    for i in range(0,len(matrix[0])):
        row = matrix[i]
        for j in range(0,i):
            if i == 0 and j == 0:
                break            
            if row[j] != 0:
                bottom = False
    return bottom

n = int(input("How many rows and coloumn in your matrix: "))

m = []
for i in range(0,n):
    row = input('Enter row: ')
    row = row.split()
    m.append(row)

y = upper_checker(m)
x = bottom_checker(m)


if y == False and x == True:
    print("This matrix is upper triangular.")
if y == True and x == False:
    print("This matrix is a lower triangular")
if y == True and x == True:
    print("This matrix is upper and lower triangular")
if y == False and x == False:       
    print('This matrix is neither upper nor lower triangular.')
