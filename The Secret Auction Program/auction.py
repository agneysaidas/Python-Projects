from art import logo

print(logo)

# Initialize an empty dictionary to store participants' bids
auction = {}

# Control variable to keep the bidding process running
add_participants = True

# Start the bidding process
while add_participants:
    name = input("What is your name?: ")
    price = int(input("What's your bid: "))
    # Store the name and bid in the auction dictionary
    auction[name] = price
    new_bid = input("Are there any other bid? type 'yes' or 'no': ").lower()
    print("\n" * 20)    
    # If there are no more bidders, end the loop and declare the winner
    if new_bid == "no":
        add_participants = False        
        # Find the name of the highest bidder using max() with auction.get as key
        winner = max(auction, key=auction.get)
        print(f'The winner is {winner} with a bid of ₹{auction[winner]}')
