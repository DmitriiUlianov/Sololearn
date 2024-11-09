a = []
a += "Pyton" # Since a is a list, adding a string to it with += will treat the string as an iterable and add each character as individual elements.
b = ["Python"]
print(a)
print(a==b)

['P', 'y', 't', 'o', 'n']
False
