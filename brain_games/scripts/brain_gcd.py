import random


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def generate_question():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    return num1, num2, gcd(num1, num2)


def main():
    print('Welcome to the Brain Games!')
    name = input("May I have your name? ")
    print(f'Hello, {name}!')
    print("Find the greatest common divisor of given numbers.")

    correct_answers_count = 0

    while correct_answers_count < 3:
        num1, num2, correct_answer = generate_question()
        print(f"Question: {num1} {num2}")
        user_answer = int(input("Your answer: "))

        if user_answer == correct_answer:
            print("Correct!")
            correct_answers_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break

    if correct_answers_count == 3:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
