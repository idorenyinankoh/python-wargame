from random import*
class Card():
    def __init__(self, carddeck):
        self.cardeck = carddeck

# class Cards():
#     def __init__(self):
# comment
    def shufflein(self):
        #shuffle(self.cardeck)
        deckA = self.cardeck[:26]
        deckB =  self.cardeck[26:]
        return deckA, deckB
    # a,b = shufflein()
    # print(a, b)

    def deckone(self, one):
        cardA=(one.pop(0))
    #rint(cardA)
        return cardA

    def decktwo(self, two):
        cardB=(two.pop(0))
        return cardB    
    
    # def chooseCard(self):
    #     card =  input('continue playing by typing yes')
    #     return card
    # r = deckone()
    # t = decktwo()
    # if r > t:
    #     print('r is bigger')
    # else:
    #     print ('t is bigger')
    #     print(r, t)      
