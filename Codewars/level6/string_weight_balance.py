"""
Each exclamation mark weight is 2; Each question mark weight is 3. 
Put two string left and right to the balance, Are they balanced?

If the left side is more heavy, return "Left"; If the right side is 
more heavy, return "Right"; If they are balanced, return "Balance".
"""
def balance(left, right):
    total_left = 0
    total_right = 0
    
    for char in left:
        if char == "!":
            total_left += 2
        elif char == "?":
            total_left += 3
    
    for char in right:
        if char == "!":
            total_right += 2
        elif char == "?":
            total_right += 3
    
    if total_left == total_right:
        return "Balance"
    elif total_left < total_right:
        return "Right"
    else:
        return "Left"
"""
Test.describe("Basic tests")

Test.assert_equals(balance("","") , "Balance")
Test.assert_equals(balance("!!","??") , "Right")
Test.assert_equals(balance("!??","?!!") , "Left")
Test.assert_equals(balance("!?!!","?!?") , "Left")
Test.assert_equals(balance("!!???!????","??!!?!!!!!!!") , "Balance")
"""
