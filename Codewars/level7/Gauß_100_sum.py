def f(n):
    x = 1
    y = n
    total = 0
    
    if n == 1:
        return 1
    else:
        while x <= 50 and y >= 51:
            total += x + y
            x += 1
            y -= 1
    
    return total
