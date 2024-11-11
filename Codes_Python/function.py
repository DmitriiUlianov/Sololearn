def decor(a,b):
    def sq(func):
        return func(a,b)*func(a,b)
    return sq
def subs(a,b):
    return (a-b)
def add(a,b):
    return (a+b)
f = decor(2,3)
print(f(add) + f(subs)) # Output: 26

'''
The code defines a decorator function, decor, which takes two arguments, a and b. 
Inside decor, there's another function sq, which applies a function (func) to a and b, then squares the result of func(a, b). 
The decor function returns the sq function.

Let's analyze what the code does step-by-step:

1. f = decor(2,3) initializes f to be the sq function with a = 2 and b = 3.

2. f(add) calls sq with the add function as func, where add(2, 3) = 5. Squaring this result, we get 25.

3. f(subs) calls sq with the subs function as func, where subs(2, 3) = -1. Squaring this result, we get 1.

The final result is f(add) + f(subs), which is 25 + 1 = 26.
'''
