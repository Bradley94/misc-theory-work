"""
Modify the kebabize function so that it converts a camel case string into a kebab case.
For example:
  kebabize('camelsHaveThreeHumps') // camels-have-three-humps
  kebabize('camelsHave3Humps') // camels-have-humps
"""

def kebabize(string):
    kebab = ""
    count = 0
    
    for letter in string:
        if letter.isupper() and letter.isalpha():
            if count == 0:
                txt = letter.lower()
                kebab += txt
                count += 1
            else:
                txt = "-" + letter.lower()
                kebab += txt
                count += 1
        elif letter.isalpha():
            kebab += letter
            count += 1
            
    return kebab

"""
Test.describe("Basic tests")
Test.assert_equals(kebabize('myCamelCasedString'), 'my-camel-cased-string')
Test.assert_equals(kebabize('myCamelHas3Humps'), 'my-camel-has-humps')
Test.assert_equals(kebabize('SOS'), 's-o-s')
Test.assert_equals(kebabize('42'), '')
Test.assert_equals(kebabize('CodeWars'), 'code-wars')
"""
