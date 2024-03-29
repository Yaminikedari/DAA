def is_palindrome(s):
   #if string has no characters or only one character then it is a palindrome.
    if len(s) <= 1:
        return True
    else:
       
        return s[0] == s[-1] and is_palindrome(s[1:-1])

input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
