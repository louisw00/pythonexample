import random


def guessanumber(x):
    guess = 0
    num = random.randint(1, x)
    while guess != num:
        guess = int(input(f"\nPlease guess a number!from 1 to 10\n"))
        if guess > num:
            print("too high")
        elif guess < num:
            print("too low")

    print("youve guessed the right nubmer")


guessanumber(10)