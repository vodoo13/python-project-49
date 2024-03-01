import prompt
GAME_ROUNDS = 3


def game_launcher(game):
    game_rule = game.GAME_RULE
    attemp = 0
    user_name = prompt.string("Welcome to the Brain Games!\
     \nMay I have your name? ")
    print(f"Hello, {user_name}!")
    print(game_rule)
    while attemp < GAME_ROUNDS:
        question, correct_answer = game.get_game()
        print(question)
        answer = prompt.string('Your answer: ')

        if correct_answer == answer:
            print('Correct!')
            attemp += 1
        else:
            print(f"{answer} is wrong answer ;(. "
                  f"Correct answer was {correct_answer}."
                  f"\nLet's try again, {user_name}!")
            return

    print(f"Congratulations, {user_name}!")
