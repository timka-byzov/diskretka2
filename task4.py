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


def f_recursive(primes_included, perm_len, lcm):
    global m, p
    for i in range(primes_included, len(p)):
        k = p[i]
        while k <= perm_len:
            f_recursive(i + 1, perm_len - k, k * lcm)
            k *= p[i]
    m = max(m, lcm)


n = int(input())
f_recursive(0, n, 1)
print(m)
