"""
Your task, is to create NxN multiplication table, of size provided in parameter.

for example, when given size is 3:

1 2 3
2 4 6
3 6 9
for given example, the return value should be: [[1,2,3],[2,4,6],[3,6,9]]
"""
def multiplication_table(size):
    i = 1
    result = []
    
    while i <= size:
        multiples = []
        j = 1
        for num in range(size):
            multiples.append(i * j)
            j += 1
        
        result.append(multiples)
        i += 1
        
    
    return result 
"""
test.describe("Basic Tests")
test.it("Should pass basic tests")
test.assert_equals(multiplication_table(3), [[1,2,3],[2,4,6],[3,6,9]])
"""
