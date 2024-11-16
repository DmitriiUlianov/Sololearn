def dec(func):
    def f(a, b):
        print("Solo", end="")
        if b == 0:
            print("Lear", end="")
            return
        return func(a, b)  # Calls the original divide function
    return f

@dec
def divide(a, b):
    print(" [Calling original divide] ", end="")
    return a / b

# Test cases
print("\nResult:", divide(3, 0))  # Output: SoloLear, Result: None
print("\nResult:", divide(6, 2))  # Output: Solo [Calling original divide] 3.0

# Output:
SoloLear
Result: None
Solo [Calling original divide] 
Result: 3.0

"""
Key Takeaways
The @dec decorator modifies the behavior of divide by:
Adding custom logic ("SoloLear") before calling the original function.
Preventing the original divide function from being called when b == 0.
The original divide function (func) is still accessible inside f and is called only if the conditions in f allow it.

In both cases, return f is executed when the @dec decorator is applied. However:
In the first case, the execution inside f exits early (return statement within the if block).
In the second case, f continues to the line where the original divide function (func) is called.
"""
