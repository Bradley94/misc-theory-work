"""
Factorial function using a while loop
"""

def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num

run_test = factorial(int(input("Enter a number: ")))
print(run_test)
