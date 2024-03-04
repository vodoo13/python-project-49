import random
import math

GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_number_prime(random_number):
    if random_number <= 1:
        return "no"

    for i in range(2, int(math.sqrt(random_number)) + 1):
        if random_number % i == 0:
            return "no"

    return "yes"


def get_game():
    random_number = random.randint(2, 100)
    question = f"Question: {random_number}"
    result = is_number_prime(random_number)
    return question, result
