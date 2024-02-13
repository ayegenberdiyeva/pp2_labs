# Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.

def gen(a, b):
    for i in range(a, b+1):
        yield i*i

a = int(input("a: "))
b = int(input("b: "))

squares = gen(a, b)

for i in squares:
    print(i)

#done