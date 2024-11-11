l = []
for i in range(17):
    l.append(i*3)
m = [x&1 for x in l]
print(l)           # [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]
print(m)           # [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
print(sum(m))      # 8

'''
m = [x & 1 for x in l]

The bitwise AND operation (&) works by comparing the binary representations of two numbers bit by bit. 
When you apply the & operation with 1, you're specifically checking the least significant bit (LSB) of the number.

Each integer in Python has a binary representation, and the least significant bit (the rightmost bit) tells us whether a number is odd or even:

Even numbers have a least significant bit of 0 (e.g., 2 is 10 in binary, 4 is 100, 6 is 110, etc.).
Odd numbers have a least significant bit of 1 (e.g., 1 is 1 in binary, 3 is 11, 5 is 101, etc.).

  0110   (binary for 6)
& 0001   (binary for 1)
--------
  0000   (result, which is 0)

For each x in the list l, this list comprehension:
Returns 1 if x is odd (because the LSB is 1).
Returns 0 if x is even (because the LSB is 0).
This creates a list m where each element is 1 if the corresponding number in l is odd, and 0 if it's even.

'''
