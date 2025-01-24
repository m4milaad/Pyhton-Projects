import random

import art

def valid_input(inp):
    while True:
        if inp.lower() in ['y','n']:
            return inp
    print("Enter valid input (y or n) : ")


def hand_and_scores(user_cards,comp_cards):
    print(f"Your final hand: {user_cards}, Final score: {total_score(user_cards)}")
    print(f"Computers final hand: {comp_cards}, Final score: {total_score(comp_cards)}")


def total_score(list_of_cards):
    if sum(list_of_cards) > 21 and 11 in list_of_cards:
        for i in range(len(list_of_cards)):
            if list_of_cards[i] == 11:
                list_of_cards[i] = 1
    return sum(list_of_cards)


def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def if_blackjack(u_cards, c_cards):
    if sum(c_cards) == 21:
        print("Computer wins by a Blackjack")
        return True
    elif sum(u_cards) == 21:
        print("User wins by a Blackjack")
        return True
    
def cards_stats(user_cards,comp_cards):
    print(f"Your cards are{user_cards} and your current score is: {total_score(user_cards)}")
    print(f"Computers first card is:  {comp_cards[0]}")


def final_result(u_cards, c_cards):
    if total_score(u_cards) > total_score(c_cards):
        hand_and_scores(u_cards,c_cards)
        print("You win")
    elif total_score(u_cards) < total_score(c_cards):
        hand_and_scores(u_cards,c_cards)
        print("Computer wins")
    else:
        hand_and_scores(u_cards,c_cards)
        print("It is a draw!")


def blackjack():
    print(art.logo)

    user_cards = []
    comp_cards = []
    for i in range(2):
        user_cards.append(deal_cards())
        comp_cards.append(deal_cards())
    if if_blackjack(user_cards, comp_cards):
        return
    cards_stats(user_cards,comp_cards)
    draw_another_card = valid_input(input("Do you want to draw another card(y or n): "))
    while draw_another_card == 'y':
        user_cards.append(deal_cards())
        if total_score(user_cards) > 21:
            hand_and_scores(user_cards,comp_cards)
            print("Computer wins")
            return
        cards_stats(user_cards,comp_cards)
        draw_another_card = valid_input(input("Do you want another card(y or n): "))

    while total_score(comp_cards) < 16:
        comp_cards.append(deal_cards())
    if total_score(comp_cards) > 21:
        hand_and_scores(user_cards,comp_cards)
        print("You win")
        return
    final_result(user_cards, comp_cards)


want_to_play = valid_input(input("Do you want to play the game of black jack(y or n): "))
while want_to_play == "y":
    print(art.logo)
    print("\n"*20)
    blackjack()
    want_to_play = valid_input(input("Do you want to play again (y or n ): "))
