"""
There are some stones on Bob's table in a row, and each of them can be red, green or blue, indicated by the characters R, G, and B.

Help Bob find the minimum number of stones he needs to remove from the table so that the stones in each pair of adjacent stones have different colours.

Examples:

"RGBRGBRGGB"   => 1
"RGGRGBBRGRR"  => 3
"RRRRGGGGBBBB" => 9
"""
def solution(s):
    return sum(1 for i in range(len(s)) if i and s[i-1]==s[i])
"""
import codewars_test as test

@test.describe("Sample tests")
def sample_tests():
    @test.it("Test 1")
    def test_1():
        test.assert_equals(solution("RGBRGBRGGB"), 1)
    @test.it("Test 2")
    def test_2():
        test.assert_equals(solution("RGGRGBBRGRR"), 3)
    @test.it("Test 3")
    def test_3():
        test.assert_equals(solution("RRRRGGGGBBBB"), 9)
"""
