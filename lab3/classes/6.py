# Write a program which can filter prime numbers in a list by using filter function. Note: Use lambda to define anonymous functions.

def is_prime(n):
    if n<2:
        return False
    for i in range(2, int(n/2)):
        if n%i == 0:
            return False
    return True

list_of_num = [1, 2, 6, 7, 3]

print("Filtered list:", list(filter(lambda x: is_prime(x), list_of_num)))

#done