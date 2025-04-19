import random
import art  

# List of possible card values in Blackjack
# 11 represents Ace, and 10 is repeated for Jack, Queen, and King
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Function to randomly select a card from the deck
def selecting_card():
    return random.choice(cards)

# Adds a card to the player's hand
def my_deck():
    my_cards.append(selecting_card())
    return my_cards

# Adds a card to the computer's hand
def computer_deck():
    computer_cards.append(selecting_card())
    return computer_cards

# Calculates the sum of cards in a hand
# Adjusts for Aces: converts one 11 to 1 if the total goes over 21
def calculate_sum(value):
    if sum(value) > 21 and 11 in value:
        value[value.index(11)] = 1
    return sum(value)

# Compares final scores and returns a result message
def compare(my_score, computer_score):
    if my_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Computer went over. You win 😁"
    elif my_score == computer_score:
        return "Draw 🙃"
    elif my_score > computer_score:
        return "You win 😎"
    else:
        return "You lose 😤"

# Main game loop: keeps running as long as the player wants to play
while input("Do you want to play a game of Black Jack? Type 'y' or 'n': ").lower() == "y":
    # Reset hands at the beginning of each game
    my_cards = []
    computer_cards = []

    # Clear the screen and show the logo
    print("\n" * 20)
    print(art.logo)

    # Initial deal: two cards each
    for i in range(2):
        my_cards = my_deck()
        computer_cards = computer_deck()

    # Player's turn
    game_over = True
    while game_over:
        my_score = calculate_sum(my_cards)
        computer_score = calculate_sum(computer_cards)

        # Display current hand and one computer card
        print(f'Your cards: {my_cards}, current score: {my_score}')
        print(f"Computer's first card: {computer_cards[0]}")

        # End turn if Blackjack or bust
        if my_score == 21 or my_score > 21:
            game_over = False
        else:
            # Ask player if they want another card
            hit = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if hit == 'y':
                my_cards = my_deck()
            else:
                game_over = False

    # Computer's turn: must draw cards until score is 17 or higher
    while calculate_sum(computer_cards) < 17:
        computer_cards = computer_deck()

    # Final results
    print(f"\nYour final hand: {my_cards}, final score: {calculate_sum(my_cards)}")
    print(f"Computer's final hand: {computer_cards}, final score: {calculate_sum(computer_cards)}")
    print(compare(calculate_sum(my_cards), calculate_sum(computer_cards)))
