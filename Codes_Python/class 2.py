class pets:
    def __init__(self,name):
        self.name = name
pet1 = pets("cat")
print(hasattr(pet1, "group")) # False
setattr(pet1, "group", "dog")
print(pet1.group) # dog
print(pet1.name) # cat


class pets:
    def __init__(self, name):
        self.name = name
''' 
Here, you're defining a class pets with an __init__ method. The __init__ method initializes the name attribute when an instance of the class is created. 
The name is set to whatever value you pass during object creation.
'''

pet1 = pets("cat")
'''
An object pet1 of class pets is created with the name "cat". The name attribute of pet1 will now be "cat".
'''

print(hasattr(pet1, "group"))
'''
The hasattr() function checks if the object pet1 has an attribute named "group". 
Since you haven't defined an attribute named group in the class pets, the result of this check will be False.
'''

setattr(pet1, "group", "dog")
'''
The setattr() function is used to dynamically add a new attribute to the pet1 object. Here, it adds the attribute group and sets its value to "dog".
Now, pet1 has a new attribute group, with the value "dog".
'''
