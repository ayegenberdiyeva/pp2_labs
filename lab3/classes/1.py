#Define a class which has at least two methods: getString: to get a string from console input printString: to print the string in upper case.

class String(object):
    def getString(self):
        string = input()

    def __int__(self, string):
        self.string = string

    def printString(self):
        print(self.string)

s = String(str(input()))
s.printString()