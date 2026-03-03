def is_palindrome(item):
    """
    Determines if a string or number is a palindrome.

    Args:
        item: The string or number to check.

    Returns:
        True if the item is a palindrome, False otherwise.
    """
    s = str(item)
    return s == s[::-1]

# Example usage:
# print(is_palindrome("madam"))      # True
# print(is_palindrome(121))         # True
# print(is_palindrome("hello"))     # False
# print(is_palindrome(12345))       # False
def add_numbers(x, y):
    """
    This function adds two numbers and returns the sum.
    """
    return x + y

