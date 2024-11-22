x = [0, 0, 0]
y = [1, 1, 1]
print(x and y) # "and" operator returns the first falsy operand if one exists; otherwise, it returns the last operand.
print(x or y)  # "or" operator returns the first truthy operand if it finds one; otherwise, it returns the last operand.

[1, 1, 1]
[0, 0, 0]


print("a" or "b") # a
print("a" and "b") # b
print("" or "a") # a
print("" and "b") # 
