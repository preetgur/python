
# findall, search, split, sub, finditer

# raw string : escape sequence character ko escape nahi kare ga
print("\n")          # new line
print(r"\n")         # raw string

import re

mobile = """ +91 99142-04589,
             +91 62841-92183
             +9198141-43615,
             +91 98141-06159,
             kdslfjklasjfkls,
             sldkjflaskdf;ldsk,
             sdfladsjlkjfds,
             +91 9855004589,
             +91 1234567895

"""

mystring = """Name : Gurpeet Singh, 
               Qualification : BTech,
               Address : vilage khandoli, Teh. Rajpura
               Email id : preetgur0137@gmail.com
               mobile no : 99142-04589"""

patt = re.compile(r'mobile')

# Meta Character
patt = re.compile(r'.')   # . : matches any charater
patt = re.compile(r'.Email')

patt = re.compile(r'^Name')  #   ^ : stars with
patt = re.compile(r'89$')  #   $ : ends with

patt = re.compile(r'ur*')  #   * : zero or more occurrences
patt = re.compile(r'ur+')  #   + : one or more occurrences

patt = re.compile(r'ur{1}')  #  {} : Excatly the specified number of occurrences
patt = re.compile(r'(ur){1}')  #  () : Capture and group

patt = re.compile(r'ur{1}| 9914204589')  #  | : Either or

# special sequences
patt = re.compile(r'\AName')  #  \A : Return a match if the specified characters are at the begning of the string

patt = re.compile(r'\bBTech')  #  \B : Return a match where the specified characters are at the begning or at the end of word
patt = re.compile(r'BTech\b') 

patt = re.compile(r'\d{5}-\d{5}') 
# Task search for mobile no

patt = re.compile(r'[+]\d{2}\s\d{5}-\d{5}') 
patt = re.compile(r'\W+\d{2}\s\d{5}-\d{5}') 



# matches = patt.finditer(mystring)
matches = patt.finditer(mobile)


for match in matches:
    print(match)
    # print(mystring[181:187])


""" 
Meta Characters
[] A set of characters
\ Signals a special sequence (can also be used to escape special characters)
. Any character (except newline character)
^ Starts with
$ Ends with
* Zero or more occurrences
+ One or more occurrences
{} Exactly the specified number of occurrences
| Either or
() Capture and group
Special Sequences
\A Returns a match if the specified characters are at the beginning of the string
\b Returns a match where the specified characters are at the beginning or at the end of a word r"ain\b"
\B Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word

\d Returns a match where the string contains digits (numbers from 0-9)
\D Returns a match where the string DOES NOT contain digits
\s Returns a match where the string contains a white space character
\S Returns a match where the string DOES NOT contain a white space character
\w Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
\W Returns a match where the string DOES NOT contain any word characters
\Z Returns a match if the specified characters are at the end of the string
"""
