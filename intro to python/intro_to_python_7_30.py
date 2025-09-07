# 1 data types, string functions, conditionals, loops, methods, classes
# References: W3Schools and Python documentation

luffy = 2 #int
ussop = 5.5 #float
nami = "pirate" #string

#list --> ordered, mutable (can be changed), allows duplicates
#zoro = [1,2,3,4,5,5]

#tuples --> ordered, immutable (cannot be changed), duplicates ok
sanji = (5,4,2,3) #tuple

#sets --> unordered, mutable (can be changed), unique (no dupes)
chopper = {2,3,4,5,4,4} #set

# print(zoro[0])
# zoro[0] = 1000000000000
# print(zoro)

# print(chopper)
#

animals = {"puppy":"brown", "kitty":"gray", "parrot":"red", "panda":"white and black"}

# print(animals["puppy"])
# print(animals.keys())
# print(animals.values())
# print(animals.items())
#

# for animal, color in animals.items():
#     print(f"This {animal} is {color}.")
#
# zoro = [1,2,3,4,5,5]
#
# for element in zoro:
#     print(str(element) + " ", end="")

grade = 90

def get_my_grade():
    if grade >= 90:
        print("You got an A")
    elif grade >= 80:
        print("You got a B")
    elif grade >= 70:
        print("You got a C")
    else:
        print("You should really rethink your life choices")

grade_2 = 80

def get_my_grade_2():
    if grade_2 < 70:
        print("You are a disappointment")
    elif grade_2 < 80:
        print("You are a rising star")
    elif grade_2 < 90:
        print("You are tremendous")
    else:
        print("You are spectacular")


turn = ""

print(turn)

import random
from enum import Enum

class Suit(Enum):
    HEART = 1
    SPADE = 2
    DIAMOND = 3
    CLUB = 4

cards = {"K":10, "Q":10,"J":10,"10":10,"9":9,"8":8,"7":7,"6":6,"5":5,"4":4,"3":3,"2":2,"A":1}

class Game:
    def __init__(self):
        self.deck = []

    def get_new_deck(self):
        for card in cards:
           self.deck.append(((Suit.HEART), card))
           self.deck.append(((Suit.SPADE), card))
           self.deck.append(((Suit.DIAMOND), card))
           self.deck.append(((Suit.CLUB), card))

        random.shuffle(self.deck)

    def deal(self):
        temp = self.deck.pop()
        return cards[temp[1]]


game = Game()
game.get_new_deck()
user = 0
comp = 0
while turn != "0":
    turn = input("Hit or hold (A or press Enter)")

    if turn == "A":
        user = game.deal()

    if comp < 17:
        comp += game.deal()

    if comp > 21:
        print("User wins!")
    elif user > 21:
        print("Computer wins!")

    if len(game.deck) == 0:
        raise Exception("Game Over")



