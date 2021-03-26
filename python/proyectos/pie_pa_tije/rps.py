from random import randint

# lista de opciones
t = ["Rock", "Paper", "Scissors"]

# asignando un elemento a la máquina
computer = t[randint(0, 2)]

player = False

while player == False:

    player = input("Rock, Paper, Scissors?")
    
    if player == computer:
        print("Empate")

    elif player == 'Rock':
        if computer == 'Paper':
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    

