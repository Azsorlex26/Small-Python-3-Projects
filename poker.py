# Currently incomplete
from abc import abstractmethod
from random import randint

class Card:
    def __init__(self, face_tag, face_value, suit_tag, suit_value):
        self.face_tag = face_tag
        self.face_value = face_value
        self.suit_tag = suit_tag
        self.suit_value = suit_value

class Player:
    def __init__(self, balance):
        self.balance = balance

    def bet(self):
        global pool
        while True:
            try:
                amount = int(input("How much? $"))
                if amount > 0:
                    if self.balance - amount >= 0:
                        pool += amount
                        self.balance -= amount
                        break
                    print("You don't have that much money.")
                    continue
                print("You have to input a value greater than 0.")
            except:
                print("You have to input an integer.")

    def all_in(self):
        global pool
        pool += self.balance
        self.balance = 0

def setup():
    raise NotImplementedError

def players_turn():
    raise NotImplementedError

def dealers_turn():
    raise NotImplementedError

while True: # The main process of the game
    pool = 0 # The amount of money the winner wins
    player1 = Player(1000)

    setup()
    players_turn()
    dealers_turn()

    if input("Would you like to play again? (y/n) ") == 'n':
        break
