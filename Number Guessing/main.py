import random
import art

EASY = 10
HARD = 5


def difficulty_set():
    difficulty = input(
        "Enter 'hard' for hard\nEnter 'easy' for easy\nChoose difficulty: ").lower()
    if difficulty == "hard":
        tries = HARD
    elif difficulty == "easy":
        tries = EASY
    else:
        print("Invalid input")
        tries = 0
    return tries


def game():
    print("\n" * 20)
    print(art.logo)
    comp = random.randint(1, 100)
    tries = difficulty_set()
    while tries:
        print(f"You have {tries} attempts remaining to guess the number.")
        user_input = int(input("Make a guess(1-100): "))
        if user_input > comp:
            print("Too High!\nGuess again")
        elif user_input < comp:
            print("Too Low!\nGuess again")
        else:
            print(f"You guessed it right.\nThe answer is {comp}")
            break
        tries -= 1
        if tries == 0:
            print("YOU LOSE!")


play = True
while play:
    game()
    choice = input("Do you want to play again(y or n): ").lower()
    if choice != "y":
        play = False
