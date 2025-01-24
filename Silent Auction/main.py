# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import art

print(art.logo)


def highest_bidder(bidder_dictionary):
    max_name = ""
    max_bid = 0
    for key in bidders:
        if bidders[key] > max_bid:
            max_name = key
            max_bid = bidders[key]
    print(f"{max_name} won the auction by bidding ${max_bid}")


bidders = {}

bidder = True
while bidder:
    name = input("Enter your name: ")
    bid = int(input("Enter your bid: $"))
    bidders[name] = bid
    print("\n" * 20)
    repeat = input("Do you have more bidders (yes or no): ").lower()
    if repeat == "no":
        bidder = False

highest_bidder(bidders)
