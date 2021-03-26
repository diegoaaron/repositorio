from random import randint

number = randint(1, 10)
number_of_guesses = 0

player_name = input("Hola, ¿Cúal es tu nombre? ")
print(f'okay! {player_name} adivina un número del 1 al 10, tendras 5 intentos')

while number_of_guesses < 5:
    guess = int(input("Ingresa un número: "))
    number_of_guesses += 1

    if guess < number:
        print('Muy bajo!')
    
    elif guess > number:
        print('Muy alto!')

    elif guess == number:
        break
    
if guess == number:
    print(f'Esa es, lo lograste en el intento {number_of_guesses}')

else:
    print(f"No acertaste, el número era {number}")

