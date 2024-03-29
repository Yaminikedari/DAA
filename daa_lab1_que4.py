def reverse_string(s): 
    # if a string has no characters or only one character the string will be returned as it is .
    if len(s) <= 1:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])

input_string = input("Enter a string: ")
reversed_string = reverse_string(input_string)
print("Reversed string:", reversed_string)
