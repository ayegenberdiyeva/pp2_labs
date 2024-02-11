#Define a class which has at least two methods: getString: to get a string from console input printString: to print the string in upper case.

class String(object):
    def __int__(self):
        self.input_string = ""

    def getString(self):
        self.input_string = str(input("Enter a string:\n"))

    def printString(self):
        print("Uppercased string:\n" + self.input_string.upper())

s = String()
s.getString()
s.printString()

#done