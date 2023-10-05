import itertools


def solution(k, tangerine):
    com = list(itertools.combinations(tangerine, k))
    res = len(set(com[0]))
    for i in com:
        if res > len(set(i)):
            res = len(set(i))
    return res


print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))
