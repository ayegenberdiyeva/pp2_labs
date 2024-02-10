#Create a python file and import some of the functions from the above 13 tasks and try to use them.

from math import pi
import random

#1
def converter(grams):
    ounces = grams / 28.3495231
    return ounces

grams = int(input())
print(converter(grams))

#2
def conversion(fahrenheit):
    centigrade = (5 / 9) * (fahrenheit - 32)
    return centigrade

fahrenheit = int(input())
print(conversion(fahrenheit))

#3
def solve(numheads, numlegs):
    numrabbits = int(numlegs/2 - numheads)
    numchickens = int(numheads - numrabbits)
    print("chickens -", numchickens, ", rabbits -", numrabbits)

numheads = 35
numlegs = 94

solve(numheads, numlegs)

#4
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

#5
def swap(s: str, index1: int, index2: int) -> str:
    if index1 == index2:
        return s
    lindex, gindex = (index1, index2) if index1 < index2 else (index2, index1)
    return s[:lindex] + s[gindex] + s[lindex + 1:gindex] + s[lindex] + s[gindex + 1:]

def permutation_helper(s, l: int, r: int, res: list[str], prefix: str): 
    print (s, l, r, res, prefix)
    if l == r:
        res.append(prefix+s[l])
        return 
    for i in range(l, r+1): 
        s1 = swap(s, l, i)
        permutation_helper(s1, l+1, r, res, prefix+s1[l]) 

def permutation(s: str):
    res = []
    permutation_helper(s, 0, len(s)-1, res, "")
    print(res, len(res))

s = input()
permutation(s)

#6
def reverses(s1):
    text = s1.split()
    for i in range(len(text) - 1, -1, -1):
        print(text[i], end = ' ')

reverses("We are ready ")

#7
def has_33(nums):
    size = len(nums) - 1
    for i in range(size):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

nums = [1, 3, 1, 3]
print(has_33(nums))

#8
def spy_game(nums):
    appearance = 0

    for i in nums:
        if i in [1, 2, 3, 4, 5, 6, 8, 9]:
            continue
        elif i == 0 and -1<appearance<2:
            appearance+=1
        elif i==7 and appearance==2:
            return True
    return False

print(spy_game([1,7,2,0,4,5,0]))

#9
def volume(r: int):
    v = (4*pi*r*r*r)/3
    return v

radius = int(input())
print(volume(radius))

#10
def unique(list: list):
    sorted_list = []

    for i in unsorted_list:
        if i not in sorted_list:
            sorted_list.append(i)
    return sorted_list

unsorted_list = [i for i in int(input()).split]
print(unique(unsorted_list))

#11
def is_palindrome(s: str):
    reverse_s = s[::-1]

    if reverse_s == s:
        return "YES"
    else:
        return "NO"
phrase = input()
print(is_palindrome(phrase))

#12
def histogram(data: list):
    for i in data:
        print('*'*i)

data = [4, 9, 7]
histogram(data)

#13
def game(rand: int, name: str):
    count = 0
    while True:
        count += 1
        num = int(input("Take a guess.\n"))
        if num < rand:
            print ("Your guess is too low.")
        elif num > rand:
            print ("Your guess is too high.")
        elif num == rand:
            print(f"Good job, {name}! You guessed my number in {count} guesses!")
            break

name = str(input(("Hello! What is your name?\n")))

print(f"Well, {name}, I am thinking of a number between 1 and 20.")
rand = random.randint(1, 20)

game(rand, name)