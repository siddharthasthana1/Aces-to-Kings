from classes.cards import Deck, Pile

######test code####
deck1 = Deck()
deck1.shuffle()
#y = deck1.distribute_to_player(2)
deck1.show_deck()
#print('lenght of deck is', len(deck1))
#print(len(y), y[0].value, y[0].suit)
c = deck1.draw_card_from_deck()
deck1.show_deck()
print(c.value, c.suit)
#------------------------

######Game procedure######
#Initiliaze game
deck = Deck()
deck.shuffle()
plyr_num = input('How many players in the game?') #must add int checker
#Create player objects and distribute cards
players_obj = []
for i in range(plyr_num):
    cards = deck.distribute_to_player(7)
    players_obj.append(Player(cards,0))
#Create pile with first card in deck
pile = Pile([])
card = deck.draw_card_from_deck()
pile.add_to_pile(card)
#Start Game
for round in range(1,14):
    turn = 1
    while




