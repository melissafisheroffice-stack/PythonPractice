
from datetime import date

#creating variables called today.  It gets the current date from your computer
today = date.today()

#creates a date object representing June 15 1996
birthday = date(1995, 6, 15)

#checks that today is actually a date
def test_today():
    assert(isinstance(today, date))

#checks that the birthday has the correct value

def test_birthday_value():
    assert birthday == date(1995, 6, 15)

#This test is a failing one as test is not a strong
def test_instance():
    assert isinstance(today, str)


"""
Imports - bring in the tools you need
Variables - stores the dates
assert is instance checks the type of a value.
"""
