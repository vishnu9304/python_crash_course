# Types of Methods
    # Regular Methods - Automatically pass the instance as the first argument (self)
    # Class Methods - Automatically pass the instance as the first argument (cls)
    # Static Methods - They don't pass anything automatically.

import datetime

class Employee:

    raise_amount = 1.04

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
    
    # regular method
    def fullname(self):
        return "{} {}".format(self.fname, self.lname)
    
    # class method
    @classmethod
    def set_raise_amt(cls, raise_amout):
        cls.raise_amount = raise_amout

    # using class methods as alternative constructors
    @classmethod
    def fom_string(cls, emp_string):
        fname, lname, pay  = emp_string.split("-")
        # this is equivalet to e1 = Employee("vishnu", "pradeep", "100000")
        return cls(fname, lname, pay)

    @staticmethod
    def isweekday(day):
        if day.weekday() == 0 or day.weekday() == 6:
            return False
        return True

day = datetime.date(2020, 2, 23)
print(Employee.isweekday(day))