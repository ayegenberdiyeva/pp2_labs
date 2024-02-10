# Write a function that accepts string from user and print all permutations of that string.

def swap(s: str, index1: int, index2: int) -> str:
    if index1 == index2:
        return s
    lindex, gindex = (index1, index2) if index1 < index2 else (index2, index1)
    return s[:lindex] + s[gindex] + s[lindex + 1:gindex] + s[lindex] + s[gindex + 1:]

def permutation_helper(s, l: int, r: int, res: list[str], prefix: str): 
    print (s, l, r, res, prefix)
    if l == r:
        res.append(prefix+s[l])
        return 
    for i in range(l, r+1): 
        s1 = swap(s, l, i)
        permutation_helper(s1, l+1, r, res, prefix+s1[l]) 

def permutation(s: str):
    res = []
    permutation_helper(s, 0, len(s)-1, res, "")
    print(res, len(res))

s = input()
permutation(s)

#done