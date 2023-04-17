def solution(clothes: list[list]):
    cnt = {}
    for i in clothes:
        if i[1] not in cnt:
            cnt[i[1]] = 1
        else:
            cnt[i[1]] += 1
    sum = 1
    for i in cnt.values():
        sum *= i+1
    return sum-1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
