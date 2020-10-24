def greet(name, owner):
    if name == owner:
        return 'Hello boss'
    else:
        return 'Hello guest'

print(greet("Clive", "Greg"))
print(greet("Clive", "Clive"))


"""
test.assert_equals(greet('Daniel', 'Daniel'), 'Hello boss')
test.assert_equals(greet('Greg', 'Daniel'), 'Hello guest')
"""
