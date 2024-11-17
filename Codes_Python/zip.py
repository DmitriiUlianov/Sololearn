'''
The zip() function in Python combines multiple iterables such as lists, tuples, strings, dict etc, into a single iterator of tuples. 
Each tuple contains elements from the input iterables that are at the same position.
'''
# Example:
names = ['John', 'Alice', 'Bob', 'Lucy']
scores = [85, 90, 78, 92]
res = zip(names, scores)
print(list(res)) # [('John', 85), ('Jane', 90), ('Tom', 78), ('Lucy', 92)]

*x, y = [1,2], [3,4], [5,6],
print(x, type(x)) # [[1, 2], [3, 4]] <class 'list'>
print(y, type(y)) # [5, 6] <class 'list'>
print(*x + [y]) # [1, 2] [3, 4] [5, 6]
print(list(zip(*x + [y]))) # [(1, 3, 5), (2, 4, 6)]
print(list(zip(*x + [y]))[1][1]) # 4

'''
The asterisk * unpacks the contents of x so that each list inside x is passed as a separate argument to the zip function.
x = [[1, 2], [3, 4]]
zip(x)  # Incorrect: Treats `x` as a single iterable, not separate lists
zip(*x)  # Correct: Unpacks `[[1, 2], [3, 4]]` into `zip([1, 2], [3, 4])`

Wrapping y in square brackets creates a single-item list so it can be concatenated with x.
print(*x + y) # [1, 2] [3, 4] 5 6 instead of expected: [1, 2] [3, 4] [5, 6]
'''
