               # x being prime test         # y testing every number up to max on x to see if it has only one divisor (itself)
prime_numbers = [x for x in range(2, 1001) if all(x % y != 0 for y in range(2, x))]