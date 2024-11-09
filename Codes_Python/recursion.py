a = [1,2]
a.append(a)
print(a)
print(a == a[2][2][2])

a = [1, 2, [...] ]
True

'''
Here, [...] represents a recursive reference to a itself, making a a self-referencing (recursive) structure. The actual structure of a is:
a = [1, 2, [1, 2, [1, 2, [1, 2, ...]]]]
a[2][2][2] refers back to a
'''
