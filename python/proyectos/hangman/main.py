from hangman import hangman
from random import randint

palabras = ['perro', 'amigo', 'colegio', 'chibolo', 'gato', 'limon', 'mandarina']


hangman(palabras[randint(0, len(palabras))])
