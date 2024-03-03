# Write a Python program with builtin function to multiply all the numbers in a list

from math import prod

def multiplication(listik):
    # for i in range(1, len(listik)):
    #     listik[0] *= listik[i]
    # return listik[0]
    result = prod(listik)
    return result

listik = [1, 2, 3, 4, 5, 6]

resultik = multiplication(listik)

print(resultik)

#done