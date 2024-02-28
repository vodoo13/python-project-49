import random


def IsPrime(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n


def main():
    print('Welcome to the Brain Games!')
    name = input("May I have your name? ")
    print(f'Hello, {name}!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    correct_answers_count = 0

    while correct_answers_count < 3:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        user_answer = input("Your answer: ").lower()

        if (IsPrime(number) and user_answer == "yes"):
            print("Correct!")
        elif (not IsPrime(number) and user_answer == "no"):
            print("Correct!")
            correct_answers_count += 1
        else:
            correct_answer = "yes" if IsPrime(number) else "no"
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break

    if correct_answers_count == 3:
        print(f"Congratulations, {name}")


if __name__ == "__main__":
    main()
