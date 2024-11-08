''' You work in a sign factory, and the machine has started printing all of the signs backwards! 
The signs have already been packed into boxes of four signs each. Every letter on every sign is capitalized, 
so if the original sign was of a palindrome (a word or phrase that is the same backwards and forwards) you can still save those signs and not have to reprint them. 
Check each box to see if you should open it up to dig out the sign you can save, or if you need to just throw the whole box in the trash. 
 
Task  
Given the four words that were supposed to be contained in each box, determine if at least one of them is of a palindrome. 
 
Input Format  
Four strings that represent the word or phrase that was supposed to be printed on the signs inside each box. 
 
Output Format  
A string that say 'Open' if at least one of the boxes is a palindrome or 'Trash' if all of the signs are misprinted. 
 
Sample Input 
CAT 
MONDAYS 
RACECAR 
TACOS 
 
Sample Output  
Open

Explanation  
RACECAR is a palindrome and is the same forwards and backwards. You will want to open this box to get that sign out. '''

import sys
word1 = input()
word2 = input()
word3 = input()
word4 = input()

if word1 == word1[::-1]:
    print("Open")
    sys.exit()
if word2 == word2[::-1]:
    print("Open")
    sys.exit()
if word3 == word3[::-1]:
    print("Open")
    sys.exit()
if word4 == word4[::-1]:
    print("Open")
    sys.exit()
    
print("Trash")