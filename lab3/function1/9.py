#Write a function that computes the volume of a sphere given its radius.

def volume(r: int):
    v = (4*3.14*r*r*r)/3
    return v

radius = int(input())
print(volume(radius))

#done