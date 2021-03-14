class HashTable:
    def __init__(self, MAX):
        self.MAX = MAX
        self.arr = [[] for i in range(MAX)]

    def get_hash(self, key):
        count = sum(ord(i) for i in key)
        return count % self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False
        for i, v in enumerate(self.arr[h]):
            if len(v) == 2 and v[0] == key:
                self.arr[h][i] = (key, value)
                found = True
        if not found:
            self.arr[h].append((key, value))

    def __getitem__(self, item):
        h = self.get_hash(item)
        for i, j in self.arr[h]:
            if i == item:
                return j
        return []

    def __delitem__(self, key):
        h = self.get_hash(key)
        for i, val in enumerate(self.arr[h]):
            if val[0] == key:
                del self.arr[h][i]


ht = HashTable(100)
print(ht.get_hash('10'))
ht['10'] = 10
print(ht.arr)
print(ht['10'])
del ht['10']
print(ht['10'])
