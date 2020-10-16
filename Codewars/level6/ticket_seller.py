"""
The new "Avengers" movie has just been released! There are a lot of people 
at the cinema box office standing in a huge line. Each of them has a single 
100, 50 or 25 dollar bill. An "Avengers" ticket costs 25 dollars.

Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.

Can Vasya sell a ticket to every person and give change if he initially has no money and sells 
the tickets strictly in the order people queue?

Return YES, if Vasya can sell a ticket to every person and give change with the bills he has at 
hand at that moment. Otherwise return NO.

Examples:
tickets([25, 25, 50]) # => YES 
tickets([25, 100]) # => NO. Vasya will not have enough money to give change to 100 dollars
tickets([25, 25, 50, 50, 100]) # => NO. Vasya will not have the right bills to give 75 dollars of change 
(you can't make two bills of 25 from one of 50)
"""
def tickets(people):
    _25s = 0
    _50s = 0
    _100s = 0
    
    for cash in people:
        if cash == 25:
            _25s += 1
            
        elif cash == 50:
            if _25s >= 1:
                _25s -= 1
                _50s += 1
            else:
                return "NO"
            
        elif cash == 100: 
            if _50s >= 1 and _25s >= 1:
                _25s -= 1
                _50s -= 1
                _100s += 1
            elif _25s >= 3:
                _25s -= 3
                _100s += 1
            else:
                return "NO"
        
    return "YES"
"""
test.assert_equals(tickets([25, 25, 50]), "YES")
test.assert_equals(tickets([25, 100]), "NO")
"""
    
    
    
