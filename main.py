from classes.cards import Deck, Pile


deck1 = Deck()
deck1.shuffle()
#y = deck1.distribute_to_player(2)
deck1.show_deck()
#print('lenght of deck is', len(deck1))
#print(len(y), y[0].value, y[0].suit)
c = deck1.draw_card_from_deck()
deck1.show_deck()
print(c.value, c.suit)