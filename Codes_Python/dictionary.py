print({True:'yes', 1:'no',1.0:'maybe'}) # Output: {True: 'maybe'}

"""
In Python dictionaries, when there are duplicate keys that are considered equal (like True, 1, and 1.0 in this case), 
only the last assigned value for that key is retained.
However, the key displayed will be the first encountered key among duplicates that share the same hash and equality.

In this case:
1. When {True: 'yes', 1: 'no', 1.0: 'maybe'} is created, Python processes each key-value pair.

2. True is initially added with the value 'yes'.

3. When 1 is encountered, it’s treated as equivalent to True because True == 1 is True, so the value for True is updated to 'no'.

4. Finally, 1.0 is also equivalent to True and 1, so the value for True is updated to 'maybe'.

Since True was the first of these keys encountered, it remains as the visible key in the dictionary.
"""
