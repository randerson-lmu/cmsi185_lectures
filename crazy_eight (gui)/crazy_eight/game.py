class Game:
    """Plays against player"""
    def __init__(self):
        self.hand = [] #initialize hand attribute to empty list
        print("Created opponent")
        
    def make_play(self, in_play):
        """Execute play for computer
        Input: in_play = card currently in play
        Output: tuple presenting the card played
        or None if no eligible cards to play"""
        #find eligible card in hand
        for card in self.hand:
            if card[0] == in_play[0]:
                self.hand.remove(card) 
                return card
            elif card[1] == in_play[1]:
                self.hand.remove(card)
                return card
            elif card[1] == "eight":
                self.hand.remove(card)
                return card
            else:
                return 

    def count(self):
        """Return number of cards in hand"""
        return len(self.hand)
            
    def add_cards(self,cards):
        """Add cards to hand. Input 'cards' is a list."""
        self.hand.extend(cards)
        
        