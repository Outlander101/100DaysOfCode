import os

new_user = True
bids = {}
while new_user:
    user = input("Enter the Name of the bidder: ")
    bid = float(input(f"Enter the bid for {user}: "))

    bids[user] = bid
    max_bid = max(bids, key=bids.get)

    add_user = input("Is there any new bidder? (Y/N)").lower()
    if add_user == 'n':
        new_user = False

    #print("/n"*1000)
    os.system('cls' if os.name == 'nt' else 'clear')

print(f"The winning bid is {bids[max_bid]} by {max_bid}")
