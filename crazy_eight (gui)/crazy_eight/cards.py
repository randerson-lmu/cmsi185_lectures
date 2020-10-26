import pygame
import os 

#change current working directory
sourceFileDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(sourceFileDir)

class Cards:
    """Map card names to images and blit image to screen"""
    cardpics = dict(
        #clubs
        aceofclubs = pygame.image.load('cardpics/clubs-a-75.png'),   #1
        aceofclubshl = pygame.image.load('cardpics/clubs-a-75hl.png'),
        twoofclubs = pygame.image.load('cardpics/clubs-2-75.png'),   #2
        twoofclubshl = pygame.image.load('cardpics/clubs-2-75hl.png'),
        threeofclubs = pygame.image.load('cardpics/clubs-3-75.png'), #3
        threeofclubshl = pygame.image.load('cardpics/clubs-3-75hl.png'),
        fourofclubs = pygame.image.load('cardpics/clubs-4-75.png'),  #4
        fourofclubshl = pygame.image.load('cardpics/clubs-4-75hl.png'),
        fiveofclubs = pygame.image.load('cardpics/clubs-5-75.png'),  #5
        fiveofclubshl = pygame.image.load('cardpics/clubs-5-75hl.png'),
        sixofclubs = pygame.image.load('cardpics/clubs-6-75.png'),   #6
        sixofclubshl = pygame.image.load('cardpics/clubs-6-75hl.png'),
        sevenofclubs = pygame.image.load('cardpics/clubs-7-75.png'), #7
        sevenofclubshl = pygame.image.load('cardpics/clubs-7-75hl.png'),
        eightofclubs = pygame.image.load('cardpics/clubs-8-75.png'), #8
        eightofclubshl = pygame.image.load('cardpics/clubs-8-75hl.png'),
        nineofclubs = pygame.image.load('cardpics/clubs-9-75.png'),  #9
        nineofclubshl = pygame.image.load('cardpics/clubs-9-75hl.png'),
        tenofclubs = pygame.image.load('cardpics/clubs-10-75.png'),  #10
        tenofclubshl = pygame.image.load('cardpics/clubs-10-75hl.png'),
        jackofclubs = pygame.image.load('cardpics/clubs-j-75.png'),  #11
        jackofclubshl = pygame.image.load('cardpics/clubs-j-75hl.png'),
        queenofclubs = pygame.image.load('cardpics/clubs-q-75.png'), #12
        queenofclubshl = pygame.image.load('cardpics/clubs-q-75hl.png'),
        kingofclubs = pygame.image.load('cardpics/clubs-k-75.png'),  #13
        kingofclubshl = pygame.image.load('cardpics/clubs-k-75hl.png'),
        #diamonds
        aceofdiamonds = pygame.image.load('cardpics/diamonds-a-75.png'),   #14
        aceofdiamondshl = pygame.image.load('cardpics/diamonds-a-75hl.png'),
        twoofdiamonds = pygame.image.load('cardpics/diamonds-2-75.png'),   #15
        twoofdiamondshl = pygame.image.load('cardpics/diamonds-2-75hl.png'),
        threeofdiamonds = pygame.image.load('cardpics/diamonds-3-75.png'), #16
        threeofdiamondshl = pygame.image.load('cardpics/diamonds-3-75hl.png'),
        fourofdiamonds = pygame.image.load('cardpics/diamonds-4-75.png'),  #17
        fourofdiamondshl = pygame.image.load('cardpics/diamonds-4-75hl.png'),
        fiveofdiamonds = pygame.image.load('cardpics/diamonds-5-75.png'),  #18
        fiveofdiamondshl = pygame.image.load('cardpics/diamonds-5-75hl.png'),
        sixofdiamonds = pygame.image.load('cardpics/diamonds-6-75.png'),   #19
        sixofdiamondshl = pygame.image.load('cardpics/diamonds-6-75hl.png'),
        sevenofdiamonds = pygame.image.load('cardpics/diamonds-7-75.png'), #20
        sevenofdiamondshl = pygame.image.load('cardpics/diamonds-7-75hl.png'),
        eightofdiamonds = pygame.image.load('cardpics/diamonds-8-75.png'), #21
        eightofdiamondshl = pygame.image.load('cardpics/diamonds-8-75hl.png'),
        nineofdiamonds = pygame.image.load('cardpics/diamonds-9-75.png'),  #22
        nineofdiamondshl = pygame.image.load('cardpics/diamonds-9-75hl.png'),
        tenofdiamonds = pygame.image.load('cardpics/diamonds-10-75.png'),  #23
        tenofdiamondshl = pygame.image.load('cardpics/diamonds-10-75hl.png'),
        jackofdiamonds = pygame.image.load('cardpics/diamonds-j-75.png'),  #24
        jackofdiamondshl = pygame.image.load('cardpics/diamonds-j-75hl.png'),
        queenofdiamonds = pygame.image.load('cardpics/diamonds-q-75.png'), #25
        queenofdiamondshl = pygame.image.load('cardpics/diamonds-q-75hl.png'),
        kingofdiamonds = pygame.image.load('cardpics/diamonds-k-75.png'),  #26
        kingofdiamondshl = pygame.image.load('cardpics/diamonds-k-75hl.png'),
        #spades
        aceofspades = pygame.image.load('cardpics/spades-a-75.png'),   #40
        aceofspadeshl = pygame.image.load('cardpics/spades-a-75hl.png'),
        twoofspades = pygame.image.load('cardpics/spades-2-75.png'),   #41
        twoofspadeshl = pygame.image.load('cardpics/spades-2-75hl.png'),
        threeofspades = pygame.image.load('cardpics/spades-3-75.png'), #42
        threeofspadeshl = pygame.image.load('cardpics/spades-3-75hl.png'),
        fourofspades = pygame.image.load('cardpics/spades-4-75.png'),  #43
        fourofspadeshl = pygame.image.load('cardpics/spades-4-75hl.png'),
        fiveofspades = pygame.image.load('cardpics/spades-5-75.png'),  #44
        fiveofspadeshl = pygame.image.load('cardpics/spades-5-75hl.png'),
        sixofspades = pygame.image.load('cardpics/spades-6-75.png'),   #45
        sixofspadeshl = pygame.image.load('cardpics/spades-6-75hl.png'),
        sevenofspades = pygame.image.load('cardpics/spades-7-75.png'), #46
        sevenofspadeshl = pygame.image.load('cardpics/spades-7-75hl.png'),
        eightofspades = pygame.image.load('cardpics/spades-8-75.png'), #47
        eightofspadeshl = pygame.image.load('cardpics/spades-8-75hl.png'),
        nineofspades = pygame.image.load('cardpics/spades-9-75.png'),  #48
        nineofspadeshl = pygame.image.load('cardpics/spades-9-75hl.png'),
        tenofspades = pygame.image.load('cardpics/spades-10-75.png'),  #49
        tenofspadeshl = pygame.image.load('cardpics/spades-10-75hl.png'),
        jackofspades = pygame.image.load('cardpics/spades-j-75.png'),  #50
        jackofspadeshl = pygame.image.load('cardpics/spades-j-75hl.png'),
        queenofspades = pygame.image.load('cardpics/spades-q-75.png'), #51
        queenofspadeshl = pygame.image.load('cardpics/spades-q-75hl.png'),
        kingofspades = pygame.image.load('cardpics/spades-k-75.png'),  #52
        kingofspadeshl = pygame.image.load('cardpics/spades-k-75hl.png'),
        #hearts
        aceofhearts = pygame.image.load('cardpics/hearts-a-75.png'),   #27
        aceofheartshl = pygame.image.load('cardpics/hearts-a-75hl.png'),
        twoofhearts = pygame.image.load('cardpics/hearts-2-75.png'),   #28
        twoofheartshl = pygame.image.load('cardpics/hearts-2-75hl.png'),
        threeofhearts = pygame.image.load('cardpics/hearts-3-75.png'), #29
        threeofheartshl = pygame.image.load('cardpics/hearts-3-75hl.png'),
        fourofhearts = pygame.image.load('cardpics/hearts-4-75.png'),  #30
        fourofheartshl = pygame.image.load('cardpics/hearts-4-75hl.png'), 
        fiveofhearts = pygame.image.load('cardpics/hearts-5-75.png'),  #31
        fiveofheartshl = pygame.image.load('cardpics/hearts-5-75hl.png'),
        sixofhearts = pygame.image.load('cardpics/hearts-6-75.png'),   #32
        sixofheartshl = pygame.image.load('cardpics/hearts-6-75hl.png'), 
        sevenofhearts = pygame.image.load('cardpics/hearts-7-75.png'), #33
        sevenofheartshl = pygame.image.load('cardpics/hearts-7-75hl.png'),
        eightofhearts = pygame.image.load('cardpics/hearts-8-75.png'), #34
        eightofheartshl = pygame.image.load('cardpics/hearts-8-75hl.png'),
        nineofhearts = pygame.image.load('cardpics/hearts-9-75.png'),  #35
        nineofheartshl = pygame.image.load('cardpics/hearts-9-75hl.png'),
        tenofhearts = pygame.image.load('cardpics/hearts-10-75.png'),  #36
        tenofheartshl = pygame.image.load('cardpics/hearts-10-75hl.png'),
        jackofhearts = pygame.image.load('cardpics/hearts-j-75.png'),  #37
        jackofheartshl = pygame.image.load('cardpics/hearts-j-75hl.png'), 
        queenofhearts = pygame.image.load('cardpics/hearts-q-75.png'),#38
        queenofheartshl = pygame.image.load('cardpics/hearts-q-75hl.png'),
        kingofhearts = pygame.image.load('cardpics/hearts-k-75.png'),  #39
        kingofheartshl = pygame.image.load('cardpics/hearts-k-75hl.png')
    )
    
    def carddisplay(self, screen, card, pos):
        return screen.blit(self.cardpics[card], pos)
