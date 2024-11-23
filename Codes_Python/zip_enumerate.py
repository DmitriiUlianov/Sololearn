a = enumerate(range(5))
a_list = list(enumerate(range(5)))
print(a)
print(a_list)
b = enumerate(range(1,5))
b_list = list(enumerate(range(1,5)))
print(b)
print(b_list)
c = list(zip(a,b))
print(c)

<enumerate object at 0x7ab502a95ee0>
[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
<enumerate object at 0x7ab502a95f80>
[(0, 1), (1, 2), (2, 3), (3, 4)]
[((0, 0), (0, 1)), ((1, 1), (1, 2)), ((2, 2), (2, 3)), ((3, 3), (3, 4))]
