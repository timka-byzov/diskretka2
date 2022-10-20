def get_next_permutation(n: int, permutation: list[int]) -> list[int]:
    i = n - 1
    while i > 0 and permutation[i - 1] >= permutation[i]:
        i -= 1
    if i <= 0:
        return list(sorted(permutation))

    j = n - 1
    while permutation[j] <= permutation[i - 1]:
        j -= 1
    permutation[i - 1], permutation[j] = permutation[j], permutation[i - 1]

    permutation[i:] = permutation[n - 1: i - 1: -1]
    return permutation


print(*get_next_permutation(int(input()), list(map(int, input().split()))))
