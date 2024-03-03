# Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt

letters = [chr(i) for i in range(65, 91)]


for i in letters:
    file = open(
        f"/Users/aminayegenberdiyeva/Desktop/test/{i}.txt",
        "w",
    )
    file.close()