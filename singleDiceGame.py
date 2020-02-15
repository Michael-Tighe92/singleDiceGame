# import random module in order to have access to random

import random

random.seed()

# function
# calculateGame determines if player or CPU wins or if draw

def calculateGame (player, CPU, count):
    if player > CPU:
        print(f"Player Wins round {count}!")
        return True
    elif CPU > player:
        print(f"CPU Wins round {count}!")
        return False
    else:
        print(f"Round {count} ends in a draw!")

# variables
playerWins = 0
CPUWins = 0
count = 0
whoWon = 0

print("----- Welcome to single dice game! ------")
print("-----           Rules              ------")
print("1.) You or CPU must reach 5 wins in order to end the game")
print("2.) Draws do not count as either a win or loss")

while playerWins < 5 and CPUWins < 5:
    count += 1
    player = random.randint(1,6)
    CPU = random.randint(1,6)
    print(f"player's die = {player}, CPU's die = {CPU}")
    whoWon = calculateGame(player,CPU,count)
    if whoWon == True:
        playerWins += 1
    elif whoWon == False:
        CPUWins += 1

if playerWins > CPUWins:
    print(f"Player won and finished the game in round {count}!!!")
else:
    print(f"CPU won and finished the game in round {count}!!!")