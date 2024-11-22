def func(alfa):
    beta = list(map(lambda x:x-1,alfa))
    return len(list(filter(lambda y: y % 3 == 0, beta)))
print(func(range(1,10))) # 3

'''
The map function applies the given lambda function (lambda x: x-1) to each element in the alfa range. 
This subtracts 1 from each number in alfa, resulting in a new list beta.

The filter function filters out the elements in beta that do not satisfy the condition y % 3 == 0, i.e., numbers divisible by 3.
'''
