# Define a functino histogram() that takes a list of integers and prints a histogram to the screen. 
# For example, histogram([4, 9, 7]) should print the following:
# ****
# *********
# *******

def histogram(data: list):
    for i in data:
        for j in range(i):
            print("*", end= '')
            
data = [4, 9, 7]
print(histogram(data))