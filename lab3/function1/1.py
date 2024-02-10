# A recipe you are reading states how many grams you need for the ingredient.
#  Unfortunately, your store only sells items in ounces. Create a function to convert 
#  grams to ounces. ounces = 28.3495231 * grams

def converter(grams):
    ounces = grams / 28.3495231
    return ounces

grams = int(input())
print(converter(grams))

#done