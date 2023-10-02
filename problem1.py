def is_palindrome(s):
    s = ''.join(char.lower()for char in s if char.isalnum())

    return s == s[::-1]

print(is_palindrome("radar"))  # True
print(is_palindrome("Hello, World!"))  # False
print(is_palindrome("A man a plan a canal Panama"))  # True