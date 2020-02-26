class Employee:
    # __init__ is equivalent to constructor, which initializes the object. 
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = 60000
        self.email = fname + "." + lname + "@yahoo.com"

    # each method(s) inside the class will automatically take the instance as the first argument.
    # if "self" is not specified you will get below error.
    '''
        TypeError: fullname() takes no arguments (1 given)
    '''
    def fullname(self):
        return "{} {}".format(self.fname, self.lname)

# e1 is an instance of class Employee
e1 = Employee("Vishnu", "Pradeep", 100000)
e2 = Employee("Mike", "Robert", 100000)
print(e1.fullname())
print(Employee.fullname(e2))