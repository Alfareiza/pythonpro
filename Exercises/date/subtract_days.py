"""
Exercise # 2 of https://www.w3resource.com/python-exercises/date-time-exercise/index.php
5. Write a Python program to subtract five days from current date.

"""
from datetime import datetime, timedelta


def subtract_days(date, quantity):
    date = date - timedelta(quantity)
    return date


date = datetime(2020, 5, 25)  # Creating date
print(subtract_days(date, 5))
