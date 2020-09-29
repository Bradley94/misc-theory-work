def check_for_factor(base, factor):
    if base % factor == 0:
        return True
    else:
        return False
        
"""
test.describe("Should return True")
test.assert_equals(check_for_factor(10, 2), True)
test.assert_equals(check_for_factor(63, 7), True)
test.assert_equals(check_for_factor(2450, 5), True)
test.assert_equals(check_for_factor(24612, 3), True)

test.describe("Should return False")
test.assert_equals(check_for_factor(9, 2), False)
test.assert_equals(check_for_factor(653, 7), False)
test.assert_equals(check_for_factor(2453, 5), False)
test.assert_equals(check_for_factor(24617, 3), False)
"""
