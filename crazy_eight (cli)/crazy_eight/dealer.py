import random

class Dealer:
    def __init__(self):
        """Initialize a dealer object"""
        #create deck of cards as list of tuples (suit, value)
        self.base_deck = []
        self.suit = ["spades","hearts","clubs","diamonds"]
        self.value = ["ace","two","three","four","five","six","seven","eight","nine","jack","queen","king"]
        for i in self.suit:
            for j in self.value:
                self.base_deck.append((i,j))

        #shuffle the base_deck
        random.shuffle(self.base_deck)

        #initialize discard deck
        ###YOUR CODE HERE
        self.discard_deck = self.base_deck[:1]
        del self.base_deck[:1]
        print("Created dealer")

    def deal_cards(self, num):
        """Remove num cards from the base_deck"""
        ### your code here 
        cards = self.base_deck[:num]
        del self.base_deck[:num]
        return cards
       
	#return the cards that were removed (as list of tuples)

    def play_card(self, card):
        """Add 'card' to discard_deck"""
        self.discard_deck.append(card) #bu 1: used [] instead of ()
        ###CODE

    def card_in_play(self):
        """Return tuple representing the card currently in play"""
        ###YOUR CODE HERe
        #return card
        return self.discard_deck[-1]
    
    def count(self):
        """Return the number of cards remaining in base deck"""
        ###YOUR CODE HERE
        return len(self.base_deck)



