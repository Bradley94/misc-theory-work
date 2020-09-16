"""
Program will always round up unless already on an integer that is a multiple of 5.

Mathematics is:		

n + (5 - n) % 5
				
With order of operations this equates to:
1) (5 - n) % 5 = x
2) n + x
"""

def round_to_next_5(n):
    return n + (5 - n) % 5

print(round_to_next_5(27)  # will round up to 30
