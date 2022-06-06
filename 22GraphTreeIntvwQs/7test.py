# A sample of how a class property was declared on the fly!

class TestAssignment:
    def __init__(self):
        self.a = 10
        self.b = 15


def addVarToObject():
    obj = TestAssignment()
    obj.c = 20                              # c is not declared in init
    return obj

def checkAssignment():
    print(addVarToObject().c)               # .c returns a value even though it is not declared in init!


checkAssignment()


