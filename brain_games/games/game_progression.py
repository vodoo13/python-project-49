import random

GAME_RULE = "What number is missing in the progression?"


def get_game():
    start = random.randint(1, 30)
    progression_length = random.randint(6, 10)
    diff = random.randint(1, 5)
    cut_position = random.randint(0, progression_length - 1)
    result = []
    for i in range(progression_length):
        result.append(start + i * diff)
    hidden_number = result[cut_position]
    result[cut_position] = '..'
    question = 'Question: ' + ' '.join([str(x) for x in result])
    return question, str(hidden_number)
