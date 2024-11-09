'''
findall	returns a list containing all matches
'''

hi = 'hitherehi'
import re
t = re.findall('hi.?', hi)
print(t)

['hit', 'hi']

'''
The regular expression pattern 'hi.?' means:
hi: Match the substring "hi".
.?: Match any single character (.) optionally (?).
So the pattern 'hi.?' will match "hi" followed by zero or one additional character.
'''

hi = 'hitherehi'
import re
t = re.findall('hi..?', hi)
print(t)

['hith']

'''
In the pattern 'hi..?', the ? applies only to the last . in the pattern, which means:
hi: Match the literal substring "hi".
.: Match any single character.
.?: Match any single character optionally.
So, 'hi..?' will match "hi" followed by one or two characters.
'''
