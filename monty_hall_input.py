def monty_hall_input() -> (int, int):
    from random import randint

    car: int = randint(0, 2)
    first_choice: int = randint(0, 2)
    return car, first_choice
