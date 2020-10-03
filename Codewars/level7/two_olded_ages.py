"""
The two oldest ages function/method needs to be completed. 
It should take an array of numbers as its argument and return the two highest 
numbers within the array. The returned value should be an array in the format [second oldest age, oldest age].

The order of the numbers passed in could be any order. The array will always include at least 2 items.
"""

def two_oldest_ages(ages):
    new_array = []
    sorted_ages = sorted(ages)
    
    new_array.append(sorted_ages[-2])
    new_array.append(sorted_ages[-1])
    
    return new_array
    
"""
Test.assert_equals(two_oldest_ages([1, 5, 87, 45, 8, 8]), [45, 87])
Test.assert_equals(two_oldest_ages([6, 5, 83, 5, 3, 18]), [18, 83])
Test.assert_equals(two_oldest_ages([10, 1]), [1, 10])
"""
