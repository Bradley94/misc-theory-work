"""
Friday 13th or Black Friday is considered as unlucky day. Calculate how many unlucky days are in the given year.

Find the number of Friday 13th in the given year.

Input: Year as an integer.

Output: Number of Black Fridays in the year as an integer.

Examples:

unluckyDays(2015) == 3
unluckyDays(1986) == 1
"""
import calendar

def unlucky_days(year):
    count = 0
    CAL = calendar.Calendar()
    
    for month in range(1, 13):
        for day in CAL.itermonthdays2(year, month):
            if day[0] == 13 and day[1] == 4:
                count += 1
    
    return count
"""
test.describe("Example Tests")

test.assert_equals(unlucky_days(2015), 3)
test.assert_equals(unlucky_days(1986), 1)
"""
