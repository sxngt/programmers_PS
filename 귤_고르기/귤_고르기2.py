def solution(k, tangerine):
    a = dict()
    for i in tangerine:
        if i in a:
            a[i] += 1
        else:
            a[i] = 1
    return a


print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))
