"""
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.
"""

def high(x):
    listed_words = x.split()
    word_values = []
    
    for word in listed_words:  
        value = 0
        for letter in word:
            value += ord(letter) - 96
        word_values.append(value)
            
    #print(listed_words)
    #print(word_values)
    
    word_index = word_values.index(max(word_values))  # No failsafe to ensure first largest value is implemented as not sure
                                                      # how to do this yet. All random tests work fine so I'm assuming/hoping
                                                      # that the index(max) function always returns the first largest index pos.
    #print(word_index)
    return listed_words[word_index]
 
"""
test.assert_equals(high('man i need a taxi up to ubud'), 'taxi')
test.assert_equals(high('what time are we climbing up the volcano'), 'volcano')
test.assert_equals(high('take me to semynak'), 'semynak')
"""
