class Player:
    """Maintains player's hand and executes plays"""
    def __init__(self):
        """Initialize a player object"""
        self.hand = [] #initialize hand attribute to empty list
        print("Created player")
        
    def display_hand(self):
        """Print the player's hand of cards"""
        print(self.hand)
        
    def make_play(self, card, in_play):
        """Process play for player
        Inputs: card = tuple representing card to play
        in_play = card currently in play
        Outputs: card = tuple representing card played
        or return None if no eligible cards"""
        if card[0] == in_play[0] or card[1] == in_play[1] or card[1] == "eight":
            self.hand.remove(card) #bug 2: need to remove card from player's hand
            return card
        else:
            return None
        
    def count(self):
        """Return number of cards in hand"""
        return len(self.hand)
    
    def add_cards(self,cards):
        """Add cards to hand. Input 'cards' is a list."""
        self.hand += cards