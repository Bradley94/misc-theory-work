"""
Your task is to remove all consecutive duplicate words from string, leaving only first words entries. For example:
"alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"

--> "alpha beta gamma delta alpha beta gamma delta"
"""
def remove_consecutive_duplicates(s):
    results =[]
    for word in s.split():
        if word not in results:
            results.append(word)
        elif results[-1] != word:  # if word isn't the same as the current last word in results, append word
            results.append(word)
    return ' '.join(results)
"""
import codewars_test as test
# TODO Write tests
import solution # or from solution import example

# test.assert_equals(actual, expected, [optional] message)
@test.describe("Example")
def test_group():
    @test.it("test case")
    def test_case():
        test.assert_equals(remove_consecutive_duplicates('alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'), 'alpha beta gamma delta alpha beta gamma delta');

"""
