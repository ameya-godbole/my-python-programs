
# Simple python program to shuffle the deck of card

# import required modules
import random, itertools

# make a deck of cards
deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))

# shuffle the cards
random.shuffle(deck)

# Now draw five cards from the deck
print("Your five cards are:")
for i in range(5):
   print(deck[i][0], "of", deck[i][1])







