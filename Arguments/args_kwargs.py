def application (fname, lname, email, company, *args, **kwargs):
    print("{} {} works at {}.  Her email is {}.".format(fname, lname, email, company))

application("Melissa", "Fisher", "test@mail.com", "fish.org")

def summerholiday (holidaytype, destination, *args, **kwargs):
    print("{} in the {}".format(holidaytype, destination))

summerholiday("Back packing", "rainforest")