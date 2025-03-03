#Name: Josette Nelson-Magruder
#Course: CIS261
#lab Title: Deck of Cards


import random

# Define a Card class to represent a playing card
class Card:
    def __init__(self, suit, rank):
        self.suit = suit 
        self.rank = rank

    
    # Return a string representation of the card
    def __str__(self):
        return f'{self.rank} of {self.suit}'


# Define a Deck class to represent a deck of 52 playing cards
class Deck:
    def __init__(self):
        self.suits = ['hearts', 'diamonds', 'clubs', 'spades']  # List of the four suits
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']  # List of the card ranks
        # Create the deck of cards by combining each rank with each suit
        self.deck = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def shuffle(self):
        # Shuffle the deck using the random.shuffle() method
        random.shuffle(self.deck)

    def deal(self, num_cards):
        # Deal the specified number of cards from the deck
        dealt_cards = []  # List to store the dealt cards
        for _ in range(num_cards):
            if self.deck:  # Check if there are cards left in the deck
                dealt_cards.append(self.deck.pop())  # Pop the top card from the deck and add it to the dealt_cards list
        return dealt_cards  # Return the list of dealt cards

    def count(self):
        # Return the number of remaining cards in the deck
        return len(self.deck)

# Main function to simulate dealing cards to the user
def main():
    deck = Deck()  # Create a new Deck object
    deck.shuffle()  # Shuffle the deck of cards
    print("Card Dealer\n")  # Print a welcome message
    print("I have shuffled a deck of 52 cards\n")  # Notify the user that the deck has been shuffled
    
    
    # Ask the user how many cards they want to be dealt
    try:
        num_cards = int(input("How many cards would you like to be dealt? "))
        if num_cards <= 0:  # Optional: Check if the number is positive
            print("Please enter a positive number.")
            return
    except ValueError:
        print("Please enter a valid integer.")  # Handle case where input is not a number
        return

    # Deal the specified number of cards and store them in dealt_cards
    dealt_cards = deck.deal(num_cards)
    print("\nHere are your cards:")  # Display the dealt cards
    for card in dealt_cards:
        print(card)  # Print each card using the __str__ method defined in the Card class
    
    # Display the number of remaining cards in the deck
    print(f"\nThere are {deck.count()} cards left in the deck.\n")
    print("Good luck!")  # Print a final message to the user

# Run the program when this script is executed
if __name__ == "__main__":
    main()  # Call the main function to start the program