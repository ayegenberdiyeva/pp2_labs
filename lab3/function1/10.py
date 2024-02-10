#Write a Python function that takes a list and returns a new list with unique elements of the first list. Note: don't use collection set.

def unique(list: list):
    sorted_list = []

    for i in unsorted_list:
        if i not in sorted_list:
            sorted_list.append(i)
    return sorted_list

unsorted_list = [1, 2, 3, 1]
print(unique(unsorted_list))