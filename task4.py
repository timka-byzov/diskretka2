def get_primes_up_to_n(n):
    primes = [True] * n
    primes[0] = primes[1] = False
    for i in range(2, n):
        if primes[i]:
            for j in range(i * i, n, i):
                primes[j] = False
    return [i for i in range(n) if primes[i]]


p = get_primes_up_to_n(150)
m = 1


def f_recursive(iter, n, prime):
    global m, p
    for i in range(iter, len(p)):
        k = p[i]
        while k <= n:
            f_recursive(i + 1, n - k, k * prime)
            k *= p[i]
    m = max(m, prime)


n = int(input())
f_recursive(0, n, 1)
print(m)
