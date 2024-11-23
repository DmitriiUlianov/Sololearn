a = 2
b = 3
c = "{a}{b}{ab}"
d = c.format(a = 4, b = 5, ab = a*b)
print(d) # 456

'''
c = "{a}{b}{ab}" — This string defines three placeholders {a}, {b}, and {ab}. These are not yet replaced by any values.
The line d = c.format(a = 4, b = 5, ab = a * b) calls the format() method on the string c. The method replaces the placeholders with the values provided.
The value of a and b inside the format() method has nothing to do with the earlier values (a=2 and b=3) outside the format() call.
a and b are evalueted inside the format() method.

In Python's str.format() method, expressions inside placeholders are not evaluated in the same way as in other contexts (e.g., inside a Python expression or function call). 
So, 6 is so called "the Non-Evaluated Placeholder Issue".
The string format method does not interpret a * b as a mathematical expression. 
Instead, the ab placeholder gets the string representation of the expression itself (a * b) rather than evaluating it.
In some versions of Python or different environments, the handling of the str.format() method might differ slightly, 
especially with regard to how expressions are evaluated inside the format() method.
To ensure proper evaluation, pre-compute expressions outside of the format() method and pass the final result to format()
'''
