
def power_of(x, n):
    if n == 0: return 1
    if n % 2 == 0 and n > 0:
        res = 1
        for i in range(int(n/2)):
            res *= x
        return res * res
    if n % 2 == 1 and n > 0:
        return x * power_of(x, n-1)
    if n < 0:
        return 1 / power_of(x, abs(n))
        
print(power_of(3, -4))