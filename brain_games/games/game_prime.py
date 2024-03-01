import random
import math

GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_number_prime(random_number):
    prime_flag = 0
    if random_number > 1:
        for i in range(2, int(math.sqrt(random_number)) + 1):
            if random_number % i == 0:
                prime_flag = 1
                break
        if not prime_flag:
            result = 'yes'
        else:
            result = 'no'
    return result


def get_game():
    random_number = random.randint(2, 100)
    question = f"Question: {random_number}"
    result = is_number_prime(random_number)
    return question, result
