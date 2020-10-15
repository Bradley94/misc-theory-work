"""
The main idea is to count all the occurring characters in a string. 
If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.
"""
import string

def count(user_string):
    if string == '':
        return {}
    
    counted = {}
    for character in list(string.ascii_letters):
        counter = 0
        counter = user_string.count(character)
        if counter > 0:
            counted[character] = counter
    
    return counted
"""
test.assert_equals(count('aba'), {'a': 2, 'b': 1})
test.assert_equals(count(''), {})
"""
