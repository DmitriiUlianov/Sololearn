a = list()
b = dict()
c = dict()
for n in range(3):
    a.append(n)
    b[n] = a
    c[n] = list(a)
    print('a', a)
    print('b', b)
    print('c', c)
print(b == c)

a [0]
b {0: [0]}
c {0: [0]}
a [0, 1]
b {0: [0, 1], 1: [0, 1]}
c {0: [0], 1: [0, 1]}
a [0, 1, 2]
b {0: [0, 1, 2], 1: [0, 1, 2], 2: [0, 1, 2]}
c {0: [0], 1: [0, 1], 2: [0, 1, 2]}
False

'''
Key Concept:
- In b[n] = a: The list a is not copied; instead, each dictionary key in b holds a reference to the same list object. 
This means that when a changes, all the values in b reflect that change.
- In c[n] = list(a): The list a is copied using list(a), meaning that each key in c holds a reference to a different list. 
Each copy reflects the state of a at that particular point in the loop.
'''
