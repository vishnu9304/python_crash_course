# special methods (or) magic methods used to emulate builtin behaviour in python.

# __repr__ and __str__

# __repr__ is meant to be an unambiguous representation of an object. It is used for debugging purpose by developers.

# __str__ readable representation of an object.

class Employee:

    raise_amt = 1.05

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)

    def applyraise(self):
        self.pay = self.pay * self.raise_amt
        return self.pay

    # __repr__ will be called if __str__ doesn't exist
    def __repr__(self):
        return "({}, {}, {})".format(self.fname, self.lname, self.pay)
   
    # __str__ is called by default. If __str__ doesn't exist if will fall back to __repr__
    # def __str__(self):
    #    return "{}".format(self.applyraise())

    __str__ = fullname
    
    # __add__ to add salaries of two employees
    def __add__(self, other):
        return self.pay + other.pay
    
    # __len__ to display the length of employee string
    def __len__(self):
        return len(self.fullname())

emp1 = Employee("vishnu", "pradeep", 50000)
emp2 = Employee("mohana", "priya", 60000)
print(emp1)
print(len(emp1))

# print(int.__add__(1, 3))
# print(str.__add__('a', 'b'))