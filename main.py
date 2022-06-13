    #from operator import truediv


import random
options = ["R", "P", "S"]
print("welcome to Rock, Paper and Scissors game. Please note that R is for Rock, P is for Paper, and S is scissors")
computer_input = random.choice(options)

while True:
    player_input = input("Pick an option: ")
    if player_input not in options:
        print ("error! invalid input")
        continue
    elif computer_input == player_input:
        print ("it's a tie! pick another option")
        continue

    if computer_input is options[0] and player_input is options[1]:
        print('player: ' + str(player_input) + ' ' + 'cpu: ' + str(computer_input))
        print("you win!")
        break

    elif computer_input is options[0] and player_input is options[2]:
        print('player: ' + str(player_input) + ' ' + 'cpu: ' + str(computer_input))
        print("oops! you lose")
        break

    elif computer_input is options[1] and player_input is options[0]:
        print('player: ' + str(player_input) + ' ' + 'cpu: ' + str(computer_input))
        print("oops! you lose")
        break

    elif computer_input is options[1] and player_input is options[2]:
        print('player: ' + str(player_input) + ' ' + 'cpu: ' + str(computer_input))
        print("you win!")
        break

    elif computer_input is options[2] and player_input is options[0]:
        print('player: ' + str(player_input) + ' ' + 'cpu: ' + str(computer_input))
        print("you win!")
        break

    elif computer_input is options[2] and player_input is options[1]:
        print('player: ' + str(player_input) + ' ' + 'cpu: ' + str(computer_input))
        print("oops! you lose")
        break

    
    