'''
You have an array of numbers.
Your task is to sort ascending odd numbers but even numbers must be on their places.

Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.

Example

sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]

**********************************************************************

Sample tests

Test.assert_equals(sort_array([5, 3, 2, 8, 1, 4]), [1, 3, 2, 8, 5, 4])
Test.assert_equals(sort_array([5, 3, 1, 8, 0]), [1, 3, 5, 8, 0])
Test.assert_equals(sort_array([]),[])

**********************************************************************
'''

def sort_array(source_array):
    if source_array == []:
        return source_array
    
    sorted_odds = sorted([n for n in source_array if n % 2])
    new_list = []
    for n in source_array:
        if n % 2:
            new_list.append(sorted_odds.pop(0))
        else:
            new_list.append(n)
    return list(new_list)
	

'''
BETTER SOLUTIONS/PRACTICES

-----------------------------------------------------------

def sort_array(arr):
  odds = sorted((x for x in arr if x % 2 != 0), reverse=True)
  return [x if x % 2 == 0 else odds.pop() for x in arr]
  
-----------------------------------------------------------

def sort_array(source_array):
    odds = iter(sorted(v for v in source_array if v % 2))
    return [next(odds) if i % 2 else i for i in source_array]
	
-----------------------------------------------------------

def sort_array(source_array):

    odds = []
    answer = []
    
    for i in source_array:
        if i % 2 > 0:
            odds.append(i)
            answer.append("X")
            
        else:
            answer.append(i)
            
    odds.sort()
    
    for i in odds:
        x = answer.index("X")
        answer[x] = i
    return answer

-----------------------------------------------------------
'''