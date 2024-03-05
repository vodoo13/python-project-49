import random
GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_number_even(number):
    return number % 2 == 0


def get_game():
    number = random.randint(1, 100)
    question = f"Question: {number}"
    result = 'yes' if is_number_even(number) else 'no'
    return question, result
