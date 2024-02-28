import random


def generate_progression():
    start = random.randint(1, 10)
    step = random.randint(1, 5)
    length = random.randint(5, 10)
    progression = [str(start + index * step) for index in range(length)]
    hidden_index = random.randint(0, length - 1)
    answer = progression[hidden_index]
    progression[hidden_index] = '..'
    question = ' '.join(progression)
    return question, answer


def main():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("What number is missing in the progression?")

    correct_answers = 0

    for _ in range(3):
        question, answer = generate_progression()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")
        if user_answer == answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{answer}'.")
            print(f"Let's try again, {name}!")
            break
    if correct_answers == 3:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
