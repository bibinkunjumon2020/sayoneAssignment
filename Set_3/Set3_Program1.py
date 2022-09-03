"""
Write a Python program to print yesterday, today, tomorrow.
"""
import datetime

today = datetime.date.today()
yesterday = today - datetime.timedelta(days = 1)
tomorrow = today + datetime.timedelta(days = 1)
print('Yesterday is ',yesterday)
print('Today is ',today)
print('Tomorrow is ',tomorrow)
print("#################")
# Two days difference
yesterday2 = today - datetime.timedelta(days = 2)
tomorrow2 = today + datetime.timedelta(days = 2)
print('2 Days Back ',yesterday2)
print('Today is ',today)
print('2 Days After',tomorrow2)