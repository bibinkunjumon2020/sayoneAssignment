"""
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.

"""

class StringHandle:
    def getString(self):
        self.string = input("Enter your input   : ")
    def printString(self):
        print(self.string.upper())

obj = StringHandle()
obj.getString()
obj.printString()

