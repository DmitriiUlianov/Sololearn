'''
The fromkeys() method returns a dictionary with the specified keys and the specified value.
dict.fromkeys(keys, value)
keys	are required. An iterable specifying the keys of the new dictionary
value	is optional. The value for all keys. Default value is None
'''

a = dict.fromkeys(range(5),1)
print(a) # {0: 1, 1: 1, 2: 1, 3: 1, 4: 1}
y = list(a.values()).count(2)
print(list(a.values())) # [1, 1, 1, 1, 1]
print(y) # 0


seq = ('a', 'b', 'c')
print(dict.fromkeys(seq)) # {'a': None, 'b': None, 'c': None}
