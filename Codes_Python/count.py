from itertools import count # import "count" from itertools
from itertools import *     # import all functions, classes, and variables
for i in count(20, -3):
    print(i)
    if i < 5:
        break

20
17
14
11
8
5
2

'''
count(20, -3) starts at 20 and decreases by 3 each time: 20, 17, 14, 11, 8, 5, 2, ...
'''
