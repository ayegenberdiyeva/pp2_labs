# Write a function that takes in a list of integers and returns True if it contains 007 in order
# def spy_game(nums):
#     pass

# spy_game([1,2,4,0,0,7,5]) --> True
# spy_game([1,0,2,4,0,5,7]) --> True
# spy_game([1,7,2,0,4,5,0]) --> False

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

#done