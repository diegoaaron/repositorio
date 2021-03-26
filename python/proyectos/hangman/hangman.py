def hangman(word):
    wrong = 0

    stages = ["",
             "_________       ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               ",
             "|_______________"]
    
    rletters = list(word)
    board = ['_'] * len(word)
    win = False

    print('Bienbenido al juego de ahorcado!')
    print('Tendras 8 intentos para adivinar las palabras')

    while wrong < len(stages) - 1:
        print("\n")
        msg = 'Adivina una letra'
        char = input(msg)

        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0:e]))

        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break

    if not win:
        print("\n".join(stages[0: wrong]))
        print(f"You lose! It was {word}")

hangman("cat")