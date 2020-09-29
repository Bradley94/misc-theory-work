def summation(num):
    total = 0
    for i in range (num+1):
        total += i
        
    return total
    
"""
@test.describe('Basic tests')
def basic_tssts():
    test.assert_equals(summation(1), 1)
    test.assert_equals(summation(8), 36)
    test.assert_equals(summation(22), 253)
    test.assert_equals(summation(100), 5050)
    test.assert_equals(summation(213), 22791)
"""
