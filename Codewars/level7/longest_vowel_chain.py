"""
The vowel substrings in the word codewarriors are o,e,a,io. The longest of these has a length of 2. 
Given a lowercase string that has alphabetic characters only (both vowels and consonants) and no spaces, 
return the length of the longest vowel substring. Vowels are any of aeiou.
"""

def solve(s):
    txt = ''
    
    for character in s:
        if character in 'aeiou':
            txt += character
        else:
            txt += ' '
    split_txt = txt.split()
    
    # using loop
    max_len = -1
    for ele in split_txt:
        if len(ele) > max_len:
            max_len = len(ele)
    
    return max_len

"""
Test.it("Basic tests")
Test.assert_equals(solve("codewarriors"),2)
Test.assert_equals(solve("suoidea"),3)
Test.assert_equals(solve("ultrarevolutionariees"),3)
Test.assert_equals(solve("strengthlessnesses"),1)
Test.assert_equals(solve("cuboideonavicuare"),2)
Test.assert_equals(solve("chrononhotonthuooaos"),5)
Test.assert_equals(solve("iiihoovaeaaaoougjyaw"),8)
"""
