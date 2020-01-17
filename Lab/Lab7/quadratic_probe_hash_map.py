from random import randrange
from collections.abc import MutableMapping


class QuadraticProbeHashMap:
    class Item:
        __slots__ = 'key', 'value'

        def __init__(self, k, v):
            self.key = k
            self.value = v

        def __eq__(self, other):
            return self.key == other.key

        def __ne__(self, other):
            return self is not other

        def __lt__(self, other):
            return self.key < other.key

    def __init__(self, cap=11, p=109345121):
        self.table = cap * [None]
        self.n = cap
        self.size = 0
        self.prime = p
        self.scale = 1 + randrange(p - 1)
        self.shift = randrange(p)

    def MAD_hash_func(self, k):
        print((hash(k) * self.scale + self.shift) % self.prime % len(self.table))
        return (hash(k) * self.scale + self.shift) % self.prime % len(self.table)

    def __len__(self):
        return self.size

    def resize(self, cap):
        old = self.table
        self.table = cap * [None]
        self.n = cap
        self.size = 0
        for item in old:
            if item is not None:
                self.__setitem__(item.key, item.value)

    def __setitem__(self, key, value):
        if self.size >= self.n // 2:
            self.resize(self.n * 2)

        hash_value = self.MAD_hash_func(key)
        item = self.table[hash_value]
        # index at hash_value is available
        if item is None:
            self.table[hash_value] = self.Item(key, value)
            self.size += 1
        # probing at slot (h + 1^2 mod N)
        else:
            i = 1
            index = (hash_value + i ** 2) % self.n
            item = self.table[index]
            # finding the available slot
            while item is not None and item.key != key:
                i += 1
                index = (index + i ** 2) % self.n
                item = self.table[index]
            # find the available slot None
            if item is None:
                self.table[index] = self.Item(key, value)
                self.size += 1
            # slot already occupied so -> update value instead of create new item
            else:
                self.table[index].value = value

    def __getitem__(self, key):
        hash_value = self.MAD_hash_func(key)
        item = self.table[hash_value]
        if item is None:
            raise KeyError('Key not found first')
        else:
            index = (hash_value + 1) % self.n
            for i in range(2, self.n):
                index = (index + i ** 2) % self.n
                item = self.table[index]
                if item is not None:
                    if item.key == key:
                        return item.value
            raise KeyError('Key not found')


    def __delitem__(self, key):
        hash_value = self.MAD_hash_func(key)
        item = self.table[hash_value]
        if item is None:
            raise KeyError('Key not found first')
        else:
            index = (hash_value + 1) % self.n
            for i in range(2, self.n):
                index = (index + i ** 2) % self.n
                item = self.table[index]
                if item is not None:
                    if item.key == key:
                        self.table[index] = None
                        self.size -= 1
                        return True
            raise KeyError('Key not found')

    def keys(self):
        # print('Keys:')
        # k = []
        # for item in self.table:
        #     if item is not None:
        #         k.append(item.key)
        # return k
        return list(self.__iter__())

    def items(self):
        print('Items:')
        for item in self.table:
            if item is not None:
                yield item.key, item.value

    def __iter__(self):
        for item in self.table:
            if item is not None:
                yield item.key

    def clear(self):
        self.table = self.n * [None]
        self.size = 0

    def __eq__(self, other):
        if len(self) != len(other):
            return False

        for item in self.table:
            if item is not None:
                try:
                    other_value = other[item.key]
                    if other_value != item.value:
                        return False
                except KeyError:
                    return False
        return True


table = QuadraticProbeHashMap()
table[0] = 'Zero'
table[11] = 'One'
# table[2] = 'Two'
# table[3] = 'Three'
# table[4] = 'Four'
# table[5] = 'Five'
print('length: {}'.format(len(table)))

print(table.keys())

for key in table:
    print('({})'.format(key))
# print('\nDelete table[1]')
# del table[1]
# print('length: {}'.format(len(table)))
# table.items()
#
# table2 = QuadraticProbeHashMap()
# table2[0] = 'Zero'
# table2[2] = 'Two'
# table2[3] = 'Three'
# table2[4] = 'Four'
# table2[5] = 'Five'
# print('\nCompare table1 == table2')
# print(table == table2)
#
# table3 = QuadraticProbeHashMap()
# table3[0] = 'Zero'
# table3[1] = 'One'
# table3[2] = 'Bookie'
# print('\nCompare table1 == table3')
# print(table == table3)
