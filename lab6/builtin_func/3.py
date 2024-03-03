# Write a Python program with builtin function that checks whether a passed string is palindrome or not.

my_string = str(input("Your string: "))
rev_my_string = "".join([i for i in reversed(my_string)]).lower()
print(rev_my_string)

if my_string.lower() == rev_my_string:
    print("Is palindrome.")
else :print("Is not Palindrome.")

#done