# Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.

def even_nums(limit):
    count = 1
    while count <= limit:
        if (count%2 == 0):
            yield count
        count += 1

n = int(input("Limit: "))
even_n = even_nums(n)

for i in even_n:
    print(i, end=", ")

#done