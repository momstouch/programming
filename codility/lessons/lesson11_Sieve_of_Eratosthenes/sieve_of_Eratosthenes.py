# https://codility.com/media/train/9-Sieve.pdf

# O(nloglogn)
def sieve(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    i = 2

    while i * i <= n:
        if sieve[i]:
            k = i * i
            while k <= n:
                sieve[k] = False
                k += i
        i += 1

    return [i for i, s in enumerate(sieve) if s]

def array_fact(n):
    f = [0] * (n + 1)
    i = 2

    while i * i <= n:
        if f[i] == 0:
            k = i * i
            while k <= n:
                if f[k] == 0:
                    f[k] = i
                k += i
        i += 1

    return f

# O(logx)
def factorization(x):
    f = array_fact(x)
    prime_factors = []

    while f[x] > 0:
        prime_factors.append(f[x])
        x = x // f[x]

    prime_factors.append(x)

    return prime_factors


print(sieve(20)) # get prime numbers from 2 to 20
print(factorization(20)) # factorize 20
