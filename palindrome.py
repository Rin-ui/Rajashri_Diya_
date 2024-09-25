def is_palindrome(s):
    # Normalize the string by converting to lowercase and removing spaces
    s = s.lower().replace(" ", "")
    return s == s[::-1]

# Test the function
test_string = "A man a plan a canal Panama"
if is_palindrome(test_string):
    print(f'"{test_string}" is a palindrome.')
else:
    print(f'"{test_string}" is not a palindrome.')
