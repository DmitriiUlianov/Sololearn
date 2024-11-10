class wow:
    def __init__(s,x):
        s.x = x
    def __add__(s,y):
        return wow(s.x - y.x)
    def __sub__(s,y):
        return wow(s.x + y.x)
    def __repr__(s):
        return str(s.x)
a = wow(5)
b = wow(7)
c = wow(3)
print(a - b + c) # Output: 9

'''
Class wow:
__init__: Initializes an instance of wow with an attribute x.

__add__: Defines the addition operation (+) for wow instances. When two wow objects are added, 
it returns a new wow object with x set to the difference of the x values (s.x - y.x).

__sub__: Defines the subtraction operation (-) for wow instances. When two wow objects are subtracted, 
it returns a new wow object with x set to the sum of the x values (s.x + y.x).

__repr__: Defines how wow objects are represented when printed. It returns the string version of the x attribute.


Instances and Operations:
a = wow(5): Creates a wow object with x = 5.
b = wow(7): Creates a wow object with x = 7.
c = wow(3): Creates a wow object with x = 3.
print(a - b + c): Performs the operations a - b and then adds c to the result.


In the method definitions of the wow class:
The self parameter is named s (instead of the usual self, but it still refers to the instance on which the method is called).
The parameter y represents the other instance (the one being added or subtracted).


Step-by-Step Execution:
1. a - b:
Calls __sub__ on a with b as the argument: a.__sub__(b).
In the __sub__ method, s refers to a and y refers to b.
The __sub__ method is defined as return wow(s.x + y.x), so it returns a new wow object with x = a.x + b.x = 5 + 7 = 12.

2. (a - b) + c:
Now, we add c to the result of a - b.
This calls __add__ on the result of a - b (which has x = 12) with c as the argument: (a - b).__add__(c).
In the __add__ method, s refers to the result of a - b (with x = 12), and y refers to c.
The __add__ method is defined as return wow(s.x - y.x), so it returns a new wow object with x = 12 - c.x = 12 - 3 = 9.

3. Printing the Result:
The final result is a wow object with x = 9.
print(a - b + c) calls __repr__, which returns the string representation of x, which is "9".

'''
