
def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

assert gcd(162, 192) == 6
