"""
Task:
Your goal is to create a function dative() (Dative() in C#) which returns the valid 
form of a valid Hungarian word w in dative case i. e. append the correct suffix nek or 
nak to the word w based on vowel harmony rules.

Vowel Harmony Rules (simplified)
When the last vowel in the word is

a front vowel (e, é, i, í, ö, ő, ü, ű) the suffix is -nek
a back vowel (a, á, o, ó, u, ú) the suffix is -nak
"""

def dative(word):
    front_vowel = ["e", "é", "i", "í", "ö", "ő", "ü", "ű"]
    back_vowel = ["a", "á", "o", "ó", "u", "ú"]
    vowels = []
    
    for character in word:
        if character in front_vowel or character in back_vowel:
            vowels.append(character)
    
    if vowels[-1] in front_vowel:
        return word + "nek"
    elif vowels[-1] in back_vowel:
        return word + "nak"
        
"""
# -*- coding: utf-8 -*-
test.describe("Example Tests")

tests = [
    # [input, expected],
    [u"ablak", u"ablaknak"],
    [u"tükör", u"tükörnek"],
    [u"keret", u"keretnek"],
    [u"otthon", u"otthonnak"],
    [u"virág", u"virágnak"],
    [u"tett", u"tettnek"],
    [u"rokkant", u"rokkantnak"],
    [u"rossz", u"rossznak"],
]

for inp, exp in tests:
    result = dative(inp)
    print("input: %s\nexpected: %s\nyour result: %s" % (inp, exp, result))
    test.assert_equals(result, exp)
    
"""
