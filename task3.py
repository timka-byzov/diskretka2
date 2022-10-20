from math import gcd


def get_blocks_lengths(s: str) -> [int]:
    result = []
    length = 1

    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            length += 1
        else:
            result.append(length)
            length = 1

    if length:
        result.append(length)

    return result


def get_common_gcd(blocs_lengths: list[int]) -> int:
    result = blocs_lengths[0]

    for i in range(1, len(blocs_lengths)):
        result = gcd(result, blocs_lengths[i])

    return result


def get_stable_sort_permutation(s: str) -> list[int]:
    s_list = [(s[i], i) for i in range(len(s))]
    s_list.sort()
    return [i + 1 for _, i in s_list]


def get_cycles_count(permutation: list[int]) -> int:
    used = [False] * len(permutation)
    result = 0

    for i in permutation:
        if not used[i - 1]:
            result += 1
            while not used[i - 1]:
                used[i - 1] = True
                i = permutation[i - 1]
    return result


def solve():
    n = int(input())
    s = input()

    s = s[:n]

    if get_common_gcd(get_blocks_lengths(s)) == get_cycles_count(get_stable_sort_permutation(s)):
        print("Yes")

    else:
        print("No")


solve()
