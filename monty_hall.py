from random import randint

def except_and_random_choice(ex1, ex2):
    return ex1

def monty_hall():
    car = randint(0, 2)
    first_choice = randint(0, 2)
    open_door = except_and_random_choice(car, first_choice)
    return True, True

print(monty_hall())
