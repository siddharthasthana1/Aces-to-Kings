import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

class Deck:
    def __init__(self):
        self.crd_dck = []
        for suitname in ['Hearts', 'Diamonds', 'Spades', 'Clubs']:
            for cardval in range(1,14):
                self.crd_dck.append(Card(suitname,cardval))

    def shuffle(self):
        return random.shuffle(self.crd_dck)

    def draw_card_from_deck(self): #take the first card from deck
        crd = self.crd_dck[0]
        self.crd_dck = self.crd_dck[1:]
        return crd

    def show_deck(self):
        for x in range(0,len(self.crd_dck)-1):
            print(self.crd_dck[x].value, 'of', self.crd_dck[x].suit)
        print (len(self.crd_dck))

    def distribute_to_player(self, cardnum):
        crds = self.crd_dck[0:cardnum]
        self.crd_dck = self.crd_dck[cardnum:]
        return crds

class Pile:
    def __init__(self, pile_list):
        self.pl_lst = pile_list

    def add_to_pile(self, crd):
        self.pl_lst = [crd] + self.pl_lst

    def draw_from_pile(self):
        crd = self.pl_lst[0]
        self.pl_lst = self.pl_lst[1:]
        return crd

    def empty_pile(self): #remove all cards except top card from pile
        crds_return = self.pl_lst[1:]
        self.pl_lst = self.pl_lst[0]
        return crds_return

    def show_pile(self):
        print(self.pl_lst)
