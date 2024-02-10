#Write a Python function that checks whether a word or phrase is palindrome or not. 
#Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam

def is_palindrome(s: str):
    reverse_s = s[::-1]

    if reverse_s == s:
        return "YES"
    else:
        return "NO"
phrase = input()
print(is_palindrome(phrase))

#done