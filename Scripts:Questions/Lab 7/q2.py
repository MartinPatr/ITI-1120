n = int(input("Enter the number of players: "))

players = []
teams = []
teams_dict = {}
players_dict = {}
for i in range(0,n):
    players.append(input("Please enter the player's name: "))
    teams.append(input("Please enter the player's team: "))
    teams_dict[teams[i]] = []
    players_dict[players[i]] = [teams[i]]
print(players_dict)
for i in range(0,len(players)):
    teams_dict[teams[i]].append(players[i])

print(teams_dict)