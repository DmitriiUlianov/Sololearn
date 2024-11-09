arr = [(5,8,0), (2,4)]
sum = []
for x, *y in arr: # This line uses iterable unpacking. For each tuple in arr, the first element is assigned to x, and the rest (if any) are collected into the list y.
    sum = sum + y
print(sum)

'''
First Iteration:
x, *y = (5,8,0) → x = 5 and y = [8, 0]
sum = [] + [8, 0] → sum = [8, 0]

Second Iteration:
x, *y = (2,4) → x = 2 and y = [4]
sum = [8, 0] + [4] → sum = [8, 0, 4]

After the loop, sum contains [8, 0, 4].
'''
