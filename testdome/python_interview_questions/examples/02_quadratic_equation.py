import math

def find_roots(a, b, c):
    det = math.sqrt(b * b - 4 * a * c)
    return ((-b + det) / (2 * a), (-b - det) / (2 * a))

assert find_roots(2, 10, 8) == (-1,-4)
