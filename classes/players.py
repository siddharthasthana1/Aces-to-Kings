

class Player:
    def __init__(self, hnd, score):
        self.hand = hnd
        self.points = score
        self.first_action = ['Draw from pile', 'Draw from deck']
        self.main_actions = ['Create new set', 'Add to existing set', 'Swap card from existing set', 'Discard']

    def add_to_hand(self, card):
        self.hand = [card] + self.hand

    def create_new_set(self):
        setsize = input('How many cards in new set?')
        newset = []
        for i in range(0, len(self.hand)):
            print(str(i)+")", self.hand[i])
        for i in range(0, setsize-1):
            newset[i] = input('Choose card no.' +str(i+1)+ 'of new set')
        return newset

    def swap_card_from_set(self,set):
        


