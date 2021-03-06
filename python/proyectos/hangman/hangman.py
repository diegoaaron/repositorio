def hangman(word):

    stages = ["_________       ",
              "|        |      ",
              "|        0      ",
              "|       /|\     ",
              "|       / \     ",
              "|               ",
              "|_______________"]
    
    wrong = 0
    rletters = list(word)
    board = ['_'] * len(word)
    win = False

    print('Bienbenido al juego de ahorcado!')
    print('Tendras 7 intentos para adivinar las palabras')

    while wrong < len(stages):
        print("\n")
        char = input('Adivina una letra: ')
        errores = True

        for palabra in  rletters:
            if palabra == char:
                indice = rletters.index(char)
                board[indice] = char
                rletters[indice] = '*'
                errores = False

        if errores:
            wrong += 1
        
        print("palabra formada: ",(" ".join(board)))
        print("errores: ", wrong)

        print("\n".join(stages[0:wrong]))

        if "_" not in board:
            print("You win! Palabra formada completamente")
            print('la palabra es', ''.join(board))
            win = True
            break

    if not win:
        print(f"Perdiste! La palabra correcta es: {word}")

