def solution(array: list):
    answer = 0
    counting = dict()
    for i in set(array):
        if i not in counting:
            counting[i] = array.count(i)
        else:
            counting[i] += 1
    if list(counting.values()).count(max(counting.values())) > 1:
        return -1
    else:
        return [k for k, v in counting.items() if v == max(counting.values())][0]

