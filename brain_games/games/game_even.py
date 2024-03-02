import random
GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_number_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def get_game():
    number = random.randint(1, 100)
    question = f"Question: {number}"
    result = is_number_even(number)
    return question, result
