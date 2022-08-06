from math import pi

def is_even(n):
    n = int(n)
    if n%2==0: return True
    return False

def cal_area(r):
    r = int(r)
    return (r**2)*round(pi,2)

def reverse_str(s):
    i = len(s)-1
    res = []
    while i >= 0:
        res.append(s[i])
        i -= 1
    res = ''.join(res)
    return res

def is_palindrome(s):
    if len(s) == 0 or len(s) == 1: return True
    if s[0] == s[-1]:
        newS = s.strip(s[0])
        return is_palindrome(newS)
    return False

