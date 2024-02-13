# Implement a generator that returns all numbers from (n) down to 0.

def  gen(n):
    for i in range(n, -1, -1):
        yield i

n = int(input("Limit: "))
reversed_list = gen(n)

for i in reversed_list:
    print(i)

#done