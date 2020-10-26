from player import Player
from game import Game
from dealer import Dealer
from cards import Cards
import pygame

print ("Done importing")

def in_play(dealer):
    """Return the card that is currently in play"""
    #print(dealer.card_in_play())
    return dealer.card_in_play()

def player_play(incard, player, dealer):
    """Process a player's move"""
    card = player.make_play(incard, in_play(dealer))
    if (card):
        dealer.play_card(card)
    else:
        if dealer.count() == 0:
            return "empty"
        else:
            card = dealer.deal_cards(1)
            player.add_cards(card)
              
def game_play(computer, dealer):
    """Process a computer's play"""
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
    """Main routine for Crazy Eight's"""
    #create player objects and data structures
    c8_dealer = Dealer()
    c8_opponent = Game()
    c8_opponent.add_cards(c8_dealer.deal_cards(7))
    c8_player = Player()
    c8_player.add_cards(c8_dealer.deal_cards(7))
    
    #setup pygame
    pygame.init()
    pygame.display.set_caption("Crazy Eights!")
    
    screen = pygame.display.set_mode((1000,700))
    screen.fill((0, 200, 0)) #set green background
    
    #display game title on screen
    font = pygame.font.Font(None, 48)
    text = font.render("Crazy Eight!", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = screen.get_rect().centerx
    screen.blit(text, textpos)
    
    pycards = Cards()
    
    print("...Setup Complete. Enjoy the game!...\n")
    
    #play game
    running = True
    while(c8_player.count() > 0 and c8_opponent.count() > 0 and running):
        
        #check for quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running == False
                
        cardinplay = in_play(c8_dealer)
        dispcard = cardinplay[1] + "of" + cardinplay[0]
        #print("\nCard In Play Is:", dispcard, "\n")
        pycards.carddisplay(screen, dispcard, (470, 250)) #card in center of screen
        
        #display user's cards
        x,y = 230, 550
        card_plot = dict()
        for card in c8_player.hand:
            dispcard = card[1] + "of" + card[0]
            card_rect = pycards.carddisplay(screen,dispcard, (x,y))
            x += 75
            card_plot[card] = card_rect
            
        #print(card_plot.keys()) 
        
        pygame.display.flip()
        
        #wait for user to select card on screen to play
        cardselect = True
        while cardselect:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x,y = event.pos
                    for card in card_plot:
                        if card_plot[card].collidepoint(x,y):
                            #print("you clicked", card)
                            cardselected = card
                            cardselect = False
                             
        #print("Calling player_play with",cardselected)
        stat = player_play(cardselected, c8_player, c8_dealer)
        if (stat == "empty"):
            print("...Deck is empty. Exiting...")
            #break
            running = False
        else:
            stat = game_play(c8_opponent,c8_dealer)
            if stat == "empty":
                print("...Deck is empty. Exiting...")
                #break
                running = False
                
        screen.fill((0, 200, 0)) #refresh background
        screen.blit(text, textpos) #label
        
    if (c8_player.count() == 0):
        print("Yay! You won!")
    elif (c8_opponent.count() == 0):
        print("Computer won. Better luck next time!")
    pygame.quit()      
            
if __name__ == "__main__":
    print("Welcome to Crazy Eights!")
    main()
    print("Thanks for playing!")
