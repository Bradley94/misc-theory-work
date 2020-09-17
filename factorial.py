def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num

value = int(input())

run = factorial(value)
print(run)
