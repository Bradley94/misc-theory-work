"""
Factorial function using recursion
"""

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

run_test = factorial(int(input("Enter a number: ")))
print(run_test)
