'''
4 parameters : number, shape, color, filling
3 possible outcomes : 

'''
import random


shapes = ['romboid', 'cilinder', 'wave']
numbers = ['1', '2', '3']
colors = ['red', 'green', 'purple']
fillings = ['full', 'empty', 'striped']

params = [numbers, shapes, colors, fillings]

param_dict = {
    'numbers' : numbers,
    'shapes' : shapes,
    'colors' : colors,
    'fillings' : fillings
}

#How to solve this coupling??

class Card():
    __slots__ = 'number','shape','color','filling'

    def __init__(self, number=None, shape=None, color=None, filling=None):   
        args = locals()
        arglist = list(args.items())[1:]

        if isinstance(number,Card):
            for i,slotted_attr in enumerate(self.__slots__):
                self.__setattr__(slotted_attr,number.__getattribute__(slotted_attr))
            return None
                

        for i,slotted_attr in enumerate(self.__slots__):
            if arglist[i][1] is None:
                self.__setattr__(slotted_attr,random.sample(params[i],1))
            else:
                self.__setattr__(slotted_attr,arglist[i][1])

                
    def __str__(self) -> str:
        s_out = '%s,  %s, %s, %s\n' % (self.number, self.shape , self.color, self.filling)
        return s_out
        
    def print_img(self):
        
        ...
    
    def __eq__(self, __o: object) -> bool:
        eq1 = self.number == __o.number
        eq2 = self.shape == __o.shape
        eq3 = self.color == __o.color
        eq4 = self.filling == __o.filling
        return eq1 and eq2 and eq3 and eq4
        #Maybe lookup table, otherwise coupling between filenames and object
    



'''
if __name__ == '__main__':
    a = Card()
    b = Card(a)
    print(a)
    print(b)
    print(a == b)
    
'''




