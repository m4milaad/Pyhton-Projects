import random

import art
import game_data

score = 0


# function that chooses random players
def choose_random_player():
    if len(game_data.data) == 0:
        print("no more players available")
        return 0
    else:
        return game_data.data.pop(random.randint(0, len(game_data.data) - 1))


# function that prints the data and vs
def print_data(c1, c2):
    print(f"Compare A: {c1["name"]}, {c1["description"]},from {c1["country"]}.")
    print(art.vs)
    print(f"Compare B: {c2["name"]}, {c2["description"]},from {c2["country"]}.")


# function that compares the data
def compare(p1, p2, c):
    global score
    if c == 'a' and p1 > p2:
        score += 1
        print(f"You're right! Current score: {score}.")
        return True
    if c == 'b' and p2 > p1:
        score += 1
        print(f"You're right! Current score: {score}.")
        return True
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        return False


can_play = True
print(art.logo)
person_1 = {}
person_2 = {}

while can_play:

    if person_1 == {}:
        person_1 = choose_random_player()
    else:
        person_1 = person_2
    person_2 = choose_random_player()
    print_data(person_1, person_2)
    user_choice = input("Who has more followers 'A' or 'B': ")
    can_play = compare(person_1["follower_count"], person_2["follower_count"], user_choice)
