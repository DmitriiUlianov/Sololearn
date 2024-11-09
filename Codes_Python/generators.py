True:
Generators can be iterated
Generators can be infinite
Generators use the yield keyword

False:
Generators can be indexed

'''
Generators in Python cannot be indexed directly because they do not store their items in memory like lists or tuples. 
Generators produce items on-the-fly, yielding one item at a time and forgetting it afterward, which is why you can't access items by index.
'''
