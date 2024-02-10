#You are given list of numbers separated by spaces. 
#Write a function filter_prime which will take list of numbers as an agrument and 
#returns only prime numbers from the list.

# list_of_nums = []
# while True:

#     temp = int(input())

#     if not temp:
#         break

#     list_of_nums.append(temp)

# for i in list_of_nums:
#     print(i)

def is_prime(num):
    if num == 1 or num == 0:
        return False
    for i in range(2,num):
        if num%i == 0:
            return False
    return True

list_of_nums = [1, 3, 6, 7, 5]

for i in list_of_nums:
    if is_prime(i) == True:
        print(i)

#done