# %%
# N мест
# количество печенек Сn в каждом месте
# M часов на то, чтобы съесть все печеньки в офисе
# минимальное количество печенек K, которое ему нужно съедать в течение часа

import math


# превышение лимита времени выполнения
def number_of_cookies_v1(M, Cn):
    min_K = math.ceil(sum(Cn) / M)
    max_K = max(Cn or [0])
    for K in range(min_K, max_K + 1):
        if sum(math.ceil(c / K) for c in Cn) <= M:
            return K
    return 0


def number_of_cookies(M, Cn):
    Cn = [c for c in Cn if c > 0]

    if len(Cn) == 0:
        return 0
    if len(Cn) > M:
        return 0
    if len(Cn) == M:
        return max(Cn)

    min_K = math.ceil(sum(Cn) / M)
    max_K = max(Cn)
    Ks = list(range(min_K, max_K + 1))

    low = 0
    high = len(Ks) - 1
    mid = 0
    last_K = float("inf")

    while low <= high:
        mid = (high + low) // 2
        K = Ks[mid]
        s = sum(math.ceil(c / K) for c in Cn)

        if s > M:
            low = mid + 1
        elif s <= M:
            high = mid - 1
            if K > last_K:
                return K
            last_K = K

    if last_K != float("inf"):
        return last_K

    return 0


assert number_of_cookies(6, [0, 0, 0]) == 0
assert number_of_cookies(6, [4, 4, 4]) == 2
assert number_of_cookies(6, [4, 4, 5]) == 3
assert number_of_cookies(3, [6, 6, 8]) == 8
assert number_of_cookies(3, []) == 0
assert number_of_cookies(1, [2, 2, 2]) == 0
assert number_of_cookies(1, [1, 1]) == 0
assert number_of_cookies(10, [1, 2, 3, 4, 5]) == 2
assert number_of_cookies(10, [1, 2, 3, 4, 5, 6, 7]) == 4
