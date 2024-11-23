print(sum({1:2, 3:4})) # 4
'''
The sum() function will sum the dictionary keys by default, not the values. Here's why:
1. The sum() function in Python iterates over the keys of the dictionary, not the values, unless explicitly told to do so. 
This is because dictionaries in Python are iterable by their keys.
2. In this case, the dictionary is {1: 2, 3: 4}. When you apply sum() to it, Python will sum the keys (1 and 3).

If you want to sum the values of the dictionary, you can use the values() method:
'''
print(sum({1: 2, 3: 4}.values())) # 6
