
from hashlib import new


palindrome = 'Roor'

def palindrome_check(str):
    str = str.lower()
    if len(str) == 0 or len(str) == 1:
        return True
    else:   
        if str[0] == str[-1]:
            new_str = str[1:-1]
            return palindrome_check(new_str)
    return False

print(palindrome_check(palindrome))