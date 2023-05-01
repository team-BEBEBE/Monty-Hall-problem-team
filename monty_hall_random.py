from random import randint

def monty_hall_input() -> (int, int):
    car: int = randint(0, 2)
    first_choice: int = randint(0, 2)
    return car, first_choice

def except_and_random_choice(ex1, ex2):
    chosen = ex1
    while chosen in (ex1, ex2):
        chosen = randint(0,2)

    return chosen 

def monty_hall():
    car, first_choice = monty_hall_input()
    open_door = except_and_random_choice(car, first_choice)
    second_choice = except_and_random_choice(first_choice, open_door)
    return car==first_choice, car==second_choice

print(monty_hall())
