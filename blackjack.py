# Currently incomplete
from random import randint

class Player: # A class that represents a player, including the dealer
    def __init__(self):
        self.hands = list() # Multiple hands can exist due to splitting
        self.hands.append(list())
        for i in range(0, 2):
            self.draw_card(0)

    def draw_card(self, hand): # Draw a random card from the deck and put it into the specified hand
        i = randint(0, len(deck) - 1)
        self.hands[hand].append(deck[i])
        del deck[i]
        if self.hand_value(hand) > 21: # If the player has gone over 21 and has an ace in their hand, set it to 1
            for card in self.hands[hand]:
                if card.value == 11:
                    card.value = 1
                    break

    def hand_value(self, hand):
        total = 0
        for card in self.hands[hand]:
            total += card.value
        return total

    def blackjack(self, hand): # Returns true if the hand has a blackjack
        return len(self.hands[hand]) == 2 and self.hand_value(hand) == 21

    def card(self, hand_number, card_number):
        return self.hands[hand_number][card_number]

    def all_cards(self, hand):
        cards = '['
        for card in hand:
            cards += card.tag
            if card is not hand[-1]: # Add a spacing if it isn't on the last element
                cards += ', '
            else:
                cards += ']'
        return cards

    def display_hand(self): # Displays info on the hand. This is the main interface for the game
        global dealer_hand
        if self is not dealer_hand: # Additionally show the dealer's first card if the player is playing
            print("\nDealer's hand:")
            print("[" + dealer_hand.card(0, 0).tag + ", ?]")
            print("Your hand:")
        else:
            print("\nDealer's final hand:")

        cards = ""
        for hand in self.hands:
            cards += self.all_cards(hand)
            if hand is not self.hands[-1]: # Add a spacing if it isn't on the last element
                cards += ', '

        print(cards) # Display all of the hand's cards

        """Commented out for now
        
        if blackjack(hand): # If the hand has a blackjack, say so. Otherwise just show the total value
            print("Blackjack!")
        else:"""
        print("Total value:", self.hand_value(0))

    def split(self):
        if len(self.hands) == 4:
            return
        
        while True:
            try:
                if len(self.hands) == 1:
                    index = 0
                else:
                    index = int(input("Which hand would you like to split? (1, " + len(self.hands)) + ") ") - 1

                if len(self.hands[index]) > 2:
                    print("That hand has more than two cards in it. Choose another one.")
                    continue

                self.hands.append(list())
                self.hands[index + 1].append(self.hands[index][1])
                del self.hands[index][1]
                draw_card[self.hands[index]]
                draw_card[self.hands[index + 1]]
                break
            except:
                print("Only a valid number can be input")

class Card: # Defines a card, which holds a point value along with a display value
    def __init__(self, tag, value):
        self.tag = tag
        self.value = value

def setup(): # Create the deck and draw two random cards for both the dealer and player
    global player_hand, dealer_hand
    for decks in range(0, 6): # Repeats by the number of decks included
        for value in range(2, 15): # Repeats by the number of card types in each deck
            for i in range(0, 4): # Repeats by the quantity of each card type
                if value <= 10:
                    deck.append(Card(str(value), value)) # Add a numbered card
                elif value != 14:
                    faces = ['J', 'Q', 'K']
                    deck.append(Card(faces[value - 11], 10)) # Add a face card (not ace)
                else:
                    deck.append(Card('A', 11)) # Add an ace

    player_hand = Player()
    dealer_hand = Player()

def players_turn(): # What happens in the player's turn. Returns false if the player bust
    global player_hand, balance, bet
    print("Your balance is $" + str(balance))
    while True:
        try:
            bet = int(input("How much would you like to bet? $"))
            if bet > balance:
                print("You don't have that much money.")
                continue
            elif bet < 0:
                print("You can't input a negative number.")
                continue
            break
        except:
            print("You can only input an integer.")

    player_hand.display_hand()
    while player_hand.hand_value(0) < 21 and input("Do you want to take a hit? y/n ") == 'y':
        player_hand.draw_card(0)
        player_hand.display_hand()
        if player_hand.hand_value(0) > 21:
            print("You've gone over 21 and bust!")
            balance -= bet
            return False
    return True

def dealers_turn(): # What happens in the dealer's turn. Prints the outcome once finished drawing cards
    global balance, bet
    while dealer_hand.hand_value(0) < 17: # The dealer has to draw cards if the value is less than 17
        dealer_hand.draw_card(0)
    dealer_hand.display_hand()

    if (dealer_hand.hand_value(0) > 21 or player_hand.hand_value(0) > dealer_hand.hand_value(0) or
        player_hand.blackjack(0) and not dealer_hand.blackjack(0)):
        print("You win!") # Player wins if they had a greater deck value, got a blackjack, or the dealer bust
        if not player_hand.blackjack(0):
            balance += bet
        else:
            balance += round(bet * 1.5)

    elif (player_hand.hand_value(0) < dealer_hand.hand_value(0) or
          dealer_hand.blackjack(0) and not player_hand.blackjack(0)):
        print("You lose!") # Same as above, but in reverse
        balance -= bet

    else:
        print("Draw!") # In the middle: neither bust and both have blackjacks or deck values are the same.

balance = 1500
init_bal = balance
bet = 0
while True: # The main process of the game. Go on forever until broken
    deck = list() # Declare the deck and hands
    player_hand = dealer_hand = None

    setup()
    if players_turn(): # Carry on with the dealer's turn if the player hasn't gone over 21
        dealers_turn()

    if balance > 0 and input("\nWould you like to play again? y/n ") == 'y':
        print()
    else:
        if balance > 0:
            print("You made a profit of $" + str(balance - init_bal))
        else:
            print("You lost everything. Better luck next time!")
        break