import random
import math
GAME_RULE = 'Find the greatest common divisor of given numbers.'


def get_game():
    random_number1 = random.randint(1, 100)
    random_number2 = random.randint(1, 100)
    question = f"Question: {random_number1} {random_number2}"
    result = math.gcd(random_number1, random_number2)
    return question, str(result)
