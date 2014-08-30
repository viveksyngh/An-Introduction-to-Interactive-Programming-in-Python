# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
deck = []
player_hand = []
dealer_hand = []
message = ""
# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand = []	# create Hand object

    def __str__(self):
        # return a string representation of a hand
        s = ""
        for h in self.hand :
            s = s + str(h) + " "
        return s
            
            
    def add_card(self, card):
            # add a card object to a hand
            self.hand.append(card) 

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        value = 0
        ace_count = 0
        for h in self.hand :
            if h.get_rank() == 'A' :
                ace_count = ace_count + 1
            value = value + VALUES[h.get_rank()]
        if ace_count == 0 :
            return value 
        else :
            if value + 10 <= 21 :
                return value + 10
            else :
                return value
   
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        i=0
        for h in self.hand :
            pos[0]=CARD_SIZE[0] + pos[0]
            #pos[1]=pos[1]+CARD_SIZE[1]*i
            card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(h.get_rank()), 
                        CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(h.get_suit()))
            canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
            i = i+1
# define deck class 
class Deck:
    def __init__(self):
            # create a Deck ob
            self.deck = []
            for s in SUITS :
                for r in RANKS :
                    card = Card(s,r)
                    self.deck.append(card)
                    

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck)   # use random.shuffle()

    def deal_card(self):
        # deal a card object from the deck
        return self.deck.pop()
    
    def __str__(self):
        pass	# return a string representing the deck
        s = ""
        for card in self.deck :
            s = s + str(card) + " "
        return s
            
       

deck = Deck()
dealer_hand = Hand()
player_hand = Hand()
#define event handlers for buttons
def deal():
    global score , outcome ,in_play,message,dealer_hand,player_hand,deck
    if in_play :
        outcome = "You went busted and lose."
        message = "New deal?" 
        score   = score - 1
        in_play = False
    else :
        #deck = Deck()
        deck.shuffle()
        dealer_hand = Hand()
        player_hand = Hand()
        player_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())
        player_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())
        #print "Dealer Hand" , dealer_hand
        #print "Player Hand" , player_hand
        outcome = ""
        message = "Hit or Stand ?"
        in_play = True

def hit():
    pass	# replace with your code below
    global outcome , in_play, score,message
    # if the hand is in play, hit the
    if in_play :
        if player_hand.get_value() <= 21 :
            player_hand.add_card(deck.deal_card())
            message = "Hit or Stand?"
        if player_hand.get_value() > 21 :
            outcome = "You went bust and lose."
            in_play = False
            score = score - 1
            message = "New Deal?"
            
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global outcome , in_play, score,message
    pass	# replace with your code below
    if in_play :
        if player_hand.get_value() > 21 :
            outcome="You went bust and lose."
            in_play = False
            score = score - 1
        else :
            while dealer_hand.get_value() < 17 :
                dealer_hand.add_card(deck.deal_card())
            if dealer_hand.get_value() > 21 :
                outcome = "Dealer went busted and You win."
                in_play = False 
                score = score + 1 
            elif player_hand.get_value() <= dealer_hand.get_value() :
                outcome = "You lose."
                score = score -1
                in_play = False
            else :
                outcome = "You Win."
                score = score + 1
                in_play = False
    message = "New Deal?"
                
            
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your
    global dealer_hand , player_hand,in_play
    canvas.draw_text("Dealer",[50,130],30,"Black","sans-serif")
    canvas.draw_text("Player",[50,330],30,"Black","sans-serif")
    dealer_hand.draw(canvas,[100,150])
    player_hand.draw(canvas,[100,350])
    card = Card("S", "A")
    #card.draw(canvas, [300, 300])
    canvas.draw_text("Blackjack",[100,80],30,"Cyan","sans-serif")
    canvas.draw_text("Score" + str(score),[400,80],30,"Black","sans-serif")
    canvas.draw_text(outcome,[250,130],25,"Black","sans-serif")
    canvas.draw_text(message,[400,330],25,"Black","sans-serif")
     
    if in_play :
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [100 + CARD_BACK_CENTER[0] + CARD_SIZE[0],150 + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
#frame.set_draw_handler(draw_text)
frame.set_draw_handler(draw)
#frame.set_draw_handler(draw_text)




# get things rolling
deal()
frame.start()


# remember to review the gradic rubric