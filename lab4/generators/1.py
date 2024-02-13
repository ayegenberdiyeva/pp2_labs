# Create a generator that generates the squares of numbers up to some number N.

def square(limit):
    count = 1
    while count <= limit:
        yield count*count
        count+=1

limit = int(input("Limit: "))
squares = square(limit)

for i in squares:
    print(i)

#done