import string
from xmlrpc.client import Boolean

from regex import P
from Deck import Deck
import Card

def fill_param(p1: string, p2: string):
    if p1 == p2:
        return p1
    else:
        param = [k for k,v in Card.param_dict.items() if p1 in v]
        return [x for x in Card.param_dict[param[0]] if (x != p1 and x!= p2) ][0]

def fill_set(c1,c2):
    args = []
    for k in c1.__slots__:
        args.append(fill_param(c1.__getattribute__(k), c2.__getattribute__(k)))

    return Card.Card(args[0], args[1], args[2], args[3])


    return 
class Board:
    __slots__ = 'cards','sets','has_set'
    def __init__(self, d: Deck, N: int = 12):
        self.cards = d.draw(N)
        self.sets = []
        self.find_sets()
        


    def add_cards(self, d: Deck, N: int = 3):
        self.cards.append(d.draw(N))
        self.find_sets()


    def find_sets(self, print_flag=True):
        self.has_set = False
        self.sets = []

        for i,f in enumerate(self.cards[0:2]):
            for j,s in enumerate(self.cards[(i+1):]):
                expectation = fill_set(f,s)
                for t in self.cards[(j+1):]:
                    if t == expectation:
                        self.sets.append([f,s,t])
                        self.has_set = True

    
    
    def remove_set(self, print=True):
            if not self.sets:
                print('There are no sets in the board')
            else:
                remaining_cards = [x for x in self.cards if x not in self.sets[0]]
                self.cards = remaining_cards
                if print:
                    print('Removed:\n')
                    for i in self.sets[0]:
                        print(i)
                    print('\n-----------\n')
                    print('Left:\n')
                    for i in remaining_cards:
                        print(i)
    def print_sets(self):
        if self.has_set:
            for s in self.sets:
                for c in s:
                    print(c)
                print('----\n')   
        else:
            print('There are no sets in the board\n')

if __name__ == '__main__':
    d = Deck()
    print(d.draw(2))
    b = Board(d)
    print(len(b.sets))
    print(len(b.cards))
    b.print_sets()