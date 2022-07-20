import string
from xmlrpc.client import Boolean
import Deck
import Card

def fill_param(p1: string, p2: string, param: string):
    if p1 == p2:
        return p1
    else:
        return [x for x in Card.param_dict[param] if x not in [p1, p2] ]

def fill_set(c1,c2):
    args = []
    for k in Card.param_dict.keys()
        args.append(fill_param)

    return Card()


    return 
class Board:
    __slots__ = 'cards' 
    def __init__(self, d: Deck.Deck, N: int = 12):
        self.cards = d.draw(N)

    def add_cards(self, d: Deck.Deck, N: int = 3):
        self.cards.append(d.draw(N))


    def has_set(self) -> Boolean:
        ...

        return #bool
    
    def remove_set(self):
        has_set = False
        sets =[]

        for f in range(len(self.cards)):
            for s in range(len(self.cards)-1):
                expectation = fill_set(self.cards[f],self.cards[s])
                for t in range(len(self.cards)-2):
                    ...

        if has_set:
            return None
        else:
            return sets