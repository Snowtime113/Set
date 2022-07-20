'''
4 parameters : number, shape, color, filling
3 possible outcomes : 

'''
import random


shapes = ['rectangle', 'cilinder', 'wave']
numbers = ['1', '2', '3']
colors = ['red', 'green', 'purple']
fillings = ['full', 'empty', 'striped']

params = [numbers, shapes, colors, fillings]

param_dict = {
    'numbers' : ['1', '2', '3'],
    'shapes' : ['rectangle', 'cilinder', 'wave'],
    'colors' : ['red', 'green', 'purple'],
    'fillings' : ['full', 'empty', 'striped']
}

#How to solve this coupling??

class Card():
    __slots__ = 'number','shape','color','filling'

    def __init__(self, number=None, shape=None, color=None, filling=None):   
        args = locals()
        arglist = list(args.items())[1:]
        for i,slotted_attr in enumerate(self.__slots__):
            if arglist[i][1] is None:
                self.__setattr__(slotted_attr,random.sample(params[i],1))
                print(self.__getattribute__(slotted_attr))
            else:
                self.__setattr__(slotted_attr,arglist[i][1])
                print(self.__getattribute__(slotted_attr))
                
    def __str__(self) -> str:
        s_out = '%s,  %s, %s, %s\n' % (self.number, self.shape , self.color, self.filling)
        return s_out
        
    def img(self):
        ...
        #Maybe lookup table, otherwise coupling between filenames and object
    




if __name__ == '__main__':
    a = Card()
    print(a.__slots__)
    print(a)
    





