import Card
import random

class Deck:
    __slots__ = 'cards' 
    def __init__(self):
        self.cards = []
        for n in Card.numbers:
            for s in Card.shapes:
                for c in Card.colors:
                    for f in Card.fillings:
                        self.cards.append(Card.Card(n,s,c,f))

    def shuffle(self):
        self.cards = random.sample(self.cards,len(self.cards))
    
    def __str__(self) -> str:
        out_s = ""
        for c in self.cards:
            out_s = out_s + c.__str__()
        return out_s


    def draw(self,N: int):
        out_cards = []
        if N > len(self.cards):
            N = len(self.cards)

        for i in range(N):
            self.shuffle()
            out_cards.append(self.cards.pop(0))
        return out_cards






if __name__ == "__main__":
    d = Deck()
    d.shuffle()
    #print(d)
    #print(len(d.cards))
    a = d.draw(4)
    print(len(d.cards))
    print(len(a))
