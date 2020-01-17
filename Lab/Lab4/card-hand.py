from Lab4 import LinkedBasedDS
PositionalList = LinkedBasedDS.PositionalList



class CardHand:
    class Card:
        def __init__(self, r, s):
            self.rank = r
            self.suit = s

        def __str__(self):
            return self.rank + ' ' + self.suit

    def __init__(self):
        self.cards = PositionalList()
        self.dict_card = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'J': 10, 'Q': 11, 'K': 12, 'A': 13}

    def add_card(self, r, s):
        c = self.Card(r, s)
        self.cards.add_last(c)

    def play(self, s, r = 1):
        floor = 13
        min = None
        for c in self.cards:
            if c.suit == s:
                if self.dict_card[c.rank] < floor:
                    if self.dict_card[c.rank] >= r:
                        min = c
                        floor = self.dict_card[c.rank]
        if min == None:
            head = self.cards._head
            for c in self.cards:
                head = head._next
                if c.suit == s:
                    print('Delete:', c)
                    d = self.cards._make_position(head)
                    self.cards.delete(d)
                    break
        else:
            print(min)

    def __iter__(self):
        for c in self.cards:
            yield c

    def all_of_suit(self, s):
        for c in self.cards:
            if c.suit == s:
                print(c)

cards = CardHand()
cards.add_card('A', 'S')
cards.add_card('2', 'S')
cards.add_card('K', 'S')

cards.add_card('Q', 'D')
cards.add_card('9', 'D')

cards.add_card('5', 'H')
cards.add_card('2', 'H')
cards.add_card('Q', 'H')

print('Cards:')
for c in cards:
    print(c)

print('\nPlay D:')
cards.play('D')

print('\nPlay S with rank at least 5:')
cards.play('S', 5)

print('\nPlay H with rank at least 13:')
cards.play('H', 13)

# cards.cards.delete(cards.cards.first())
print('\nCards:')
for c in cards:
    print(c)

print('\nAll of suit S')
cards.all_of_suit('S')

print('\nAll of suit D')
cards.all_of_suit('D')

print('\nAll of suit H')
cards.all_of_suit('H')