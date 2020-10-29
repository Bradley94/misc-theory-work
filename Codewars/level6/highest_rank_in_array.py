"""
Complete the method which returns the number which is most frequent in the given input array. 
If there is a tie for most frequent number, return the largest number among them.

Note: no empty arrays will be given.
"""
# https://www.geeksforgeeks.org/python-find-most-frequent-element-in-a-list/  theory for this 
# Solution 1
from collections import Counter

def highest_rank(List):
    counter = 0
    List.sort()  # order by size so largest number is always checked first
    num = List[0]
    
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency >= counter):
            counter = curr_frequency
            num = i
    
    return num

"""
test.describe("Example Tests")
test.it("Example Test Case")
test.assert_equals(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12]), 12)
test.assert_equals(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 10]), 10)
"""
