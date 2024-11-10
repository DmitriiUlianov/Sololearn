a = [1,2,3]
def add(n):
    #global a
    a += [n]
add(4)
print(a)

# Output: UnboundLocalError: cannot access local variable 'a' where it is not associated with a value
