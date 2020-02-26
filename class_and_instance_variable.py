class Employee:

    # class variables are the variables that are shared by all instances of the class.
    raise_amount = 1.04

    # number of employees. increment this class variable whenever a new instance of a class is created.
    num_of_employees = 0

    def __init__(self, fname, lname, pay):
        # instance variables are the data that are unique to each instance of the class.
        self.fname = fname
        self.lname = lname
        self.pay = pay
        Employee.num_of_employees += 1
    
    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)

    def applyraise(self):
        self.pay = self.pay * Employee.raise_amount

e1 = Employee("vishnu", "pradeep", 500000)
print("{}'s pay before applying raise: {}".format(e1.fullname(), e1.pay))
e1.applyraise()
print("{}'s pay after applying raise: {}".format(e1.fullname(), e1.pay))
print(e1.__dict__)
# print "e1" object namespace
'''
    {'lname': 'pradeep', 'pay': 520000.0, 'fname': 'vishnu'}
'''
print(Employee.__dict__)
'''
    {'__module__': '__main__', 'applyraise': <function applyraise at 0x105606ed8>, 'raise_amount': 1.04, 'fullname': <function fullname at 0x1056067d0>, '__doc__': None, '__init__': <function __init__ at 0x1056061b8>}
'''
e2 = Employee("Mike", "Robert", 500000)
print(Employee.num_of_employees)