# import random module in order to have access to random

import random

random.seed()

# functions
# calculateGame determines if player or CPU wins or if draw

def calculateGame (player, CPU, cnt):
    if player > CPU:
        print(f"Player Wins round {cnt}!")
        return True
    elif CPU > player:
        print(f"CPU Wins round {cnt}!")
        return False
    else:
        print(f"Round {cnt} ends in a draw!")

# variables
playerWins = 0
CPUWins = 0
cnt = 1
whoWon = 0

print("----- Welcome to single dice game! ------")
print("-----           Rules              ------")
print("1.) You or CPU must reach 5 wins in order to end the game")
print("2.) Draws do not count as either a win or loss")

while playerWins < 5 and CPUWins < 5:
    player = random.randint(1,6)
    CPU = random.randint(1,6)
    print(f"player's die = {player}, CPU's die = {CPU}")
    whoWon = calculateGame(player,CPU,cnt)
    if whoWon == True:
        playerWins += 1
    elif whoWon == False:
        CPUWins += 1
    cnt += 1

if playerWins > CPUWins:
    print(f"Player won and finished the game in round {cnt}!!!")
else:
    print(f"CPU won and finished the game in round {cnt}!!!")