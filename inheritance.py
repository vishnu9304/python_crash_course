# Inheritance allows us to inherit the attributes and methods from parent class.
# Note: Every class in python inherits from base object called builtins.object. 
class Employee:
    raise_amount = 1.04
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)
    def apply_raise(self):
        self.pay = self.pay * self.raise_amount
    @classmethod
    def update_raise_amount(cls, raise_amount):
        cls.raise_amount = raise_amount
# Developer inherits Employee.
# Developer object will look for attributes and methods locally first, then it will look under parent class.
# This chain is called method resolution order.
# Hint: help(Developer) will print method resolution order.
class Developer(Employee):
    # Changing the "raise_amount" in sub class will not have any effect on parent class.
    raise_amount = 1.10
    def __init__(self, fname, lname, pay, lang):
        # super().__init__(fname, lname, pay)
        Employee.__init__(self,fname, lname, pay)
        self.lang = lang
class Manager(Employee):
    def __init__(self, fname, lname, pay, employees=None):
        # super().__init__(fname, lname, pay)
        Employee.__init__(self,fname, lname, pay)
        if employees == []:
            self.employees = []
        else:
            self.employees = employees
    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_employee(self, emp):
        if emp in self.employees:
                self.employees.remove(emp)
    def print_employees(self):
        for emp in self.employees:
            print(emp.fullname())
d1 = Developer("nitin", "deepak", 100000, "go")
m1 = Manager("vishnu", "pradeep", 90000, [])
m1.add_employee(d1)
# m1.remove_employee(d1)
m1.print_employees()

## Python has two builtin function for playing around inheritance

## isinstance(instance, class)
## issubclass(class1, class2)

print(isinstance(m1, Manager))              # True
print(issubclass(Manager, Employee))        # True
print(issubclass(Employee, Manager))        # False