import random

import art


# add hand_and_score_def

def total_score(list_of_cards):
    if sum(list_of_cards) > 21 and 11 in list_of_cards:
        for i in range(len(list_of_cards)):
            if list_of_cards[i] == 11:
                list_of_cards[i] = 1
    return sum(list_of_cards)


def if_blackjack(u_cards, c_cards):
    if sum(c_cards) == 21:
        print("Computer wins by a Blackjack")
        return
    if sum(u_cards) == 21:
        print("User wins by a Blackjack")
        return


def final_result(u_cards, c_cards):
    if total_score(u_cards) > total_score(c_cards):
        print(f"Your final hand: {u_cards}, Final score: {total_score(u_cards)}")
        print(f"Computers final hand: {c_cards}, Final score: {total_score(c_cards)}")
        print("You win")
    elif total_score(u_cards) > total_score(c_cards):
        print(f"Your final hand: {u_cards}, Final score: {total_score(u_cards)}")
        print(f"Computers final hand: {c_cards}, Final score: {total_score(c_cards)}")
        print("Computer wins")
    else:
        print(f"Your final hand: {u_cards}, Final score: {total_score(u_cards)}")
        print(f"Computers final hand: {c_cards}, Final score: {total_score(c_cards)}")
        print("It is a draw!")


def blackjack():
    print(art.logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_cards = []
    comp_cards = []
    for i in range(2):
        user_cards.append(random.choice(cards))
        comp_cards.append(random.choice(cards))
    if if_blackjack(user_cards, comp_cards):
        return
    print(f"Your cards are{user_cards} and your current score is: {total_score(user_cards)}")
    print(f"Computers first card is:  {comp_cards[0]}")
    draw_another_card = input("Do you want to draw another card(y or n): ").lower()
    while draw_another_card == 'y':
        user_cards.append(random.choice(cards))
        if total_score(user_cards) > 21:
            print(f"Your final hand: {user_cards}, Final score: {total_score(user_cards)}")
            print(f"Computers final hand: {comp_cards}, Final score: {total_score(comp_cards)}")
            print("Computer wins")
            return
        print(f"Your cards are{user_cards} and your current score is: {total_score(user_cards)}")
        print(f"Computers first card is:  {comp_cards[0]}")
        draw_another_card = input("Do you want another card(y or n): ").lower()

    while total_score(comp_cards) < 16:
        comp_cards.append(cards)
    if total_score(comp_cards) > 21:
        print(f"Your final hand: {user_cards}, Final score: {total_score(user_cards)}")
        print(f"Computers final hand: {comp_cards}, Final score: {total_score(comp_cards)}")
        print("You win")
        return
    final_result(user_cards, comp_cards)


want_to_play = input("Do you want to play the game of black jack(y or n): ").lower()
while want_to_play == "y":
    print("\n"*20)
    blackjack()
    want_to_play = input("Do you want to play again (y or n ): ").lower()
