def func(x):
    x[0] = ['def']
    x[1] = ['abc']
    return id(x)
q = ['abc','def']
print(id(q) == func(q))

True

'''
The id of q does not change because func modifies the contents of the list but not the list itself. 
Therefore, the comparison id(q) == func(q) will return True, as q and x refer to the same object in memory.
'''

