"""
WIP https://www.codewars.com/kata/5f7c38eb54307c002a2b8cc8/train/python

In this kata you are given a string for example:

"example(unwanted thing)example"
Your task is to remove everything inside the parentheses as well as the parentheses themselves.

The example above would return:

"exampleexample"
Other than parentheses only letters and spaces can occur in the string. Don't worry about other brackets like
"[]" and "{}" as these will never appear.
"""

def remove_parentheses(s):
    start = []
    end = []
    
    for character in s:
        if character != '(':
            start.append(character)
        else:
            break
    
    for character in reversed(s):
        if character != ')':
            end.append(character)
        else:
            break
    
    # create return string
    txt = ''
    txt2 = ''
    
    for character in start:
        txt += character
    for character in reversed(end):
        txt2 += character
    
    return txt + txt2
            
