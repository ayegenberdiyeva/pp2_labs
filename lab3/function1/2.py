#Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade 
#temperature. The following formula is used for the conversion: C = (5 / 9) * (F – 32)

def conversion(fahrenheit):
    centigrade = (5 / 9) * (fahrenheit - 32)
    return centigrade

fahrenheit = int(input())
print(conversion(fahrenheit))

#done