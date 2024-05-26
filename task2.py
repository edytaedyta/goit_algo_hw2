from collections import deque

def is_palindrome(input_string):

    normalized_string = ''.join(char.lower() for char in input_string if char.isalnum())
    
   
    char_deque = deque(normalized_string)
    
    
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    
    return True

# Example usage:
print(is_palindrome("A man a plan a canal Panama"))
print(is_palindrome("This is not a palindrome"))                 
print(is_palindrome("Hello, World!"))                