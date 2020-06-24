# property decorators allows us to access the class methods like normal attributes.

class Employee:

    def __init__(self, first):
        self.first = first

    @property
    def get_firstname(self):
        return self.first

    @get_firstname.setter
    def get_firstname(self, first):
        self.first = first

    @get_firstname.deleter
    def get_firstname(self):
        print("Deleted!")
        self.first = None

e1 = Employee("vishnu")
print(e1.first)
e1.get_firstname = "pradeep"
print(e1.first)
print(e1.__dict__)
del e1.get_firstname
print(e1.__dict__)

"""
    v01@Vishnus-Mac oops$ python decorators.py 
    vishnu
    pradeep
    {'first': 'pradeep'}
    Deleted!
    {'first': None}
"""
