from random import shuffle 
class Card:
    def __init__(self,value ,suit ):
        self.value =value
        self.suit = suit
        #
    def __repr__(self):
         return f"{self.value} of {self.suit}"





class Deck:
        def __init__(self):
            suits =("Hearts", "Diamonds", "Clubs",  "Spades")
            values =("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
            self.cards =[Card(value,suit)for value in values for suit in suits]

        def __repr__(self):
             return f"Deck of {self.count()} cards"

        def count(self):
             return len(self.cards)
        
        def _deal(self, num):
             count = self.count()
             realmin = min([count,num])#
             if realmin == 0:
                  raise ValueError("Deste de kart kalmadi")
             cards = self.cards[-realmin:] 
             self.cards = self.cards[:-realmin]  
             return cards  
        def shuffle(self):
             if self.count()<52:
                  raise ValueError ("Sadece bütün bir deste karilabilir")
             shuffle(self.cards)
        def deal_card(self):
             return self._deal(1)[0] 
        def deal_hand(self,size):
             return self._deal(size)       



d = Deck()
d.shuffle()
card = d.deal_card()
print(card)
