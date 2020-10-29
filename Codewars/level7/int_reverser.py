"""
Impliment the reverse function, which takes in input n and reverses it. 
For instance, reverse(123) should return 321. 
You should do this without converting the inputted number into a string.
"""
# Theory on how the equation works
# https://stackoverflow.com/questions/53688984/reversing-an-integer-without-using-reverse-functions-or-lists
# https://www.programiz.com/python-programming/methods/built-in/divmod

def reverse(n):
    m = 0
    while n > 0:
        n, r = divmod(n, 10)
        m = 10 * m + r
    return m
"""
test.assert_equals(reverse(1234), 4321)
test.assert_equals(reverse(10987), 78901)
test.assert_equals(reverse(1020), 201)
"""
