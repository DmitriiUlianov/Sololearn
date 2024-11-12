def fun(egg):
    if len(egg):
        yield egg[-1]
        yield from fun(egg[:-1])
print(''.join(fun("stressed"))) # Output: desserts

'''
This code reverses the string "stressed" using a recursive generator function.

Here's a breakdown of how it works:
1. The function fun takes an argument egg, a string.
2. If egg is not empty (if len(egg):), it:
- Yields the last character (egg[-1]).
- Recursively calls fun with egg[:-1] (the string without the last character), yielding each character in reverse order.
3. ''.join(fun("stressed")) joins the yielded characters into a single reversed string.

'''
