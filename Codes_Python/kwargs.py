def func(**qwerty):
    print(qwerty["one"]) # 173
    print(qwerty) # {'a': 0, 'one': 173}
func(a = 0, one = 173)

'''
In Python, the double asterisk (**) has a special meaning when used in function definitions and function calls. It is used for collecting and unpacking keyword arguments.
**kwargs or **<name>:
**kwargs tells Python to collect any keyword arguments passed to the function and put them into a dictionary named kwargs.

The function func is defined to accept arbitrary keyword arguments using the **qwerty syntax. 
This means any keyword arguments passed to func will be collected into a dictionary and assigned to qwerty.

When the function func is called, two keyword arguments are passed:
a = 0
one = 173

These keyword arguments are collected into a dictionary by the **qwerty syntax. So, inside the function, qwerty will be:
{'a': 0, 'one': 173}

Inside the function, print(qwerty["one"]) is executed.
Since qwerty is the dictionary {'a': 0, 'one': 173}, qwerty["one"] retrieves the value associated with the key "one", which is 173.
'''
