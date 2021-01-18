import mod_games, mod_food, mod_person
import random

if __name__ == "__main__":
    m = random.choice([mod_games, mod_food, mod_person])
    m.madlib()

