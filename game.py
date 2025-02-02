"""

I’m thinking of a number between 1 and 100…

What is it?
It’s 50! But what if it were more random?

In a file called game.py, implement a program that:

Prompts the user for a level,
. If the user does not input a positive integer, the program should prompt again.
Randomly generates an integer between 1 and
, inclusive, using the random module.
Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
If the guess is larger than that integer, the program should output Too large! and prompt the user again.
If the guess is the same as that integer, the program should output Just right! and exit.

"""
import random
def main():
    game_level()

def game_level():
    while True:
        try:
            level = int(input("Level: "))
            number = []
            for l in range(level):
                number.append(l)
            choice = random.choice(number)
            return guess_number(int(choice))
        except ValueError:
            pass
        except IndexError:
            pass

def guess_number(n):
    while True:
        try:
            guess = int(input("Guess: "))
            if n > 0:
                if guess < n:
                    print("Too small!")
                elif guess > n:
                    print("Too large!")
                else:
                    print("Just right!")
                    break
        except ValueError:
            pass


if __name__ == "__main__":
    main()

