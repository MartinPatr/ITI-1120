import random
from time import sleep

#Collecting the inputs
n = int(input("How many rows: "))
maze = []
for i in range(0,n):
    row = input("Enter Row: ")
    maze.append(row)

#Prints the maze
for i in range(0,len(maze)):
    print(maze[i])

#Finds entrance
for i in range(0,len(maze)):   
    if maze[i][0] == "p":
        entrance = i
        break

#Find Exit
for i in range(0,len(maze)):
    if maze[i][-1] == "p":
        exit = i
        break

#Setting Variables
found_path = False
directions = []
dead_list = [False,False,False,False]
count = temp_count = 0
maze_run = maze.copy()
#While loop which does not leave until found_path is found
#Each time this loop is run it starts a new run
while found_path == False:
    if temp_count > count:
        count = temp_count
        directions = temp_directions.copy()
        dead_list = [False,False,False,False]
    #Print Statements for Debugging
    print("Temp:",temp_count," Count:",count)
    print(directions)
    for i in range(0,len(maze)):
        print(maze_run[i])
    print()
    sleep(0.8)
    #Setting Variabes
    y = entrance
    x = 0
    maze_run = maze.copy()
    dead_end = False
    temp_count = round = 0
    temp_directions = []    
    z = dead_list.count(True)
    if z == 4:
        directions = []
        count = 0
    #While loop which does not leave until it hits a wall
    while dead_end == False:
        #If statement checking if we follow old best or check random direction
        if round < len(directions) and len(directions) > 0:
            direction = directions[round]
        else:
            direction = random.randint(0,3)
        #Direction CHoices
        if direction == 0:
            if y == 0:
                break
            if maze_run[y-1][x] == 'p':
                maze_run[y] = maze_run[y][:x] + '^' + maze_run[y][x+1:]
                y = y - 1
                temp_count += 1
                temp_directions.append(direction)
            else:
                dead_list[0] = True
                dead_end = True
        if direction == 1:
            if y == len(maze) - 1:
                break
            if maze_run[y+1][x] == 'p':
                maze_run[y] = maze_run[y][:x] + 'v' + maze_run[y][x+1:]
                y = y + 1
                temp_count += 1
                temp_directions.append(direction)
            else:
                dead_list[1] = True
                dead_end = True    
        if direction == 2:
            if x == 0:
                break
            if maze_run[y][x-1] == 'p':
                maze_run[y] = maze_run[y][:x] + '<' + maze_run[y][x+1:]
                x = x - 1
                temp_count += 1
                temp_directions.append(direction)
            else:
                dead_list[2] = True
                dead_end = True
        if direction == 3:
            if y == exit and x == len(maze[i])-1:
                found_path = True
                maze_run[y] = maze_run[y][:x] + '>' + maze_run[y][x+1:]
                break
            if maze_run[y][x+1] == 'p':
                maze_run[y] = maze_run[y][:x] + '>' + maze_run[y][x+1:]
                x = x + 1
                temp_count += 1
                temp_directions.append(direction)
            else:
                dead_list[3] = True
                dead_end = True
        #Tracking the rounds
        round = round + 1

#Prints the maze
print("Final Maze")
for i in range(0,len(maze)):
   print(maze_run[i])