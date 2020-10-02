"""
It's your duty to verify that n is a valid positive integer number. If not, please, return false 
(None for Python, null for C#).

"""
#  S = n(n+1) / 2
         
def f(n):
    if isinstance(n, int) and n >= 1:
        return (n / 2) * (n + 1)
    else: 
        return None
      
