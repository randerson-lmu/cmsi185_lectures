from IPython.display import clear_output
from player import Player
from game import Game
from dealer import Dealer

def in_play(dealer):
    return dealer.card_in_play()

def player_play(player, dealer):
    player.display_hand()
    inCard = input("\nPick a card from your hand by typing <suit> <value>\nType 'quit' to exit:  ")
    if inCard == "quit":
        return "quit"
    else:
        if (inCard == "") :
            inCard = "blank blank"
			
        inCard = tuple(inCard.split())
        card = player.make_play(inCard, in_play(dealer))
        if (card):
            dealer.play_card(card)
        else:
            if dealer.count() == 0:
                return "empty"
            else:
                card = dealer.deal_cards(1)
                player.add_cards(card)
                
def game_play(computer, dealer):
    card = computer.make_play(in_play(dealer))
    if (card):
        dealer.play_card(card)
    else:
        if dealer.count() == 0:
            return "empty"
        else:
            card = dealer.deal_cards(1)
            computer.add_cards(card)
            
def main():
    c8_dealer = Dealer()
    c8_opponent = Game()
    c8_opponent.add_cards(c8_dealer.deal_cards(7))
    c8_player = Player()
    c8_player.add_cards(c8_dealer.deal_cards(7))
    print("...Setup Complete. Enjoy the game!...\n")
    
    while(c8_player.count() > 0 and c8_opponent.count() > 0):
    #clear_output(wait=True)
        print("\nCard In Play Is:", in_play(c8_dealer),"\n")
        stat = player_play(c8_player, c8_dealer)
        if (stat == "empty"):
            print("...Deck is empty. Exiting...")
            break
        elif (stat == "quit"):
            print("...Quiting...")
            break
        stat = game_play(c8_opponent,c8_dealer)
        if stat == "empty":
            print("...Deck is empty. Exiting...")
            break
    
        if (c8_player.count() == 0):
            print("Yay! You won!")
        elif(c8_opponent.count() == 0):
            print("Computer won. Better luck next time!")
			
if __name__ == "__main__":
    print("Welcome to Crazy Eight's!")
    main()
    print("Thanks for playing!")