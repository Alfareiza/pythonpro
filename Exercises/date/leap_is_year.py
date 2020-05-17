"""
Exercise # 2 of https://www.w3resource.com/python-exercises/date-time-exercise/index.php
 - Write a Python program to determine whether a given year is a leap year
"""


def calc_year_leap(year):
    if (year/4).is_integer():
        return True
    else:
        return False


print(calc_year_leap(2004))
