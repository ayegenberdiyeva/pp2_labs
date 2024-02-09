#Write a function that accepts string from user, 
#return a sentence with the words reversed. We are ready -> ready are We

def reverses(s1):
    text = s1.split()
    for i in range(len(text) - 1, -1, -1):
        print(text[i], end = ' ')

reverses("We are ready ")

#done