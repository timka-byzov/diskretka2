from math import factorial as fact


def canonical_permutation(permutation: list[int]) -> list[str]:
    used = [False] * len(permutation)
    result = []

    for i in permutation:
        if not used[i - 1]:
            sub_perm = []
            while not used[i - 1]:
                used[i - 1] = True
                sub_perm.append(i)
                i = permutation[i - 1]

            max_elem_idx = sub_perm.index(max(sub_perm))
            sub_perm = sub_perm[max_elem_idx:] + sub_perm[:max_elem_idx]
            result.append(sub_perm)

    result.sort(key=lambda x: x[0])

    return list(map(lambda x: '( ' + ' '.join(map(str, x)) + ' )', result))


def get_t_permutation(permutation: list[int], nth_perm: int) -> list[int]:
    result = []
    permutations_count = fact(len(permutation))
    sorted_permutation = list(sorted(permutation))

    for _ in range(len(permutation)):
        container_size = permutations_count // len(sorted_permutation)
        container_idx = nth_perm // container_size
        if nth_perm % container_size != 0:
            result.append(sorted_permutation.pop(container_idx))
            nth_perm %= container_size
        else:
            result.append(sorted_permutation.pop(container_idx - 1))
            nth_perm = container_size

        permutations_count = container_size

    return result


def solution():
    n = int(input())
    t = int(input())

    permutation = list(range(1, n + 1))
    t_perm = get_t_permutation(permutation, t)

    print(*canonical_permutation(t_perm))


solution()
