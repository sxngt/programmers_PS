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

print(solution([1]))

'''
출제의도는 총 두가지로 예상
1. 중복값을 카운팅하고, 예외를 포용할 수 있는 구현능력이나 계획성이 있는가 ?
2. 중복값을 강조하고 있는 문제에서도 counting에 사고가 묶이지 않고 다른 풀이를 떠올려볼 수 있는가 ?

위는 1번 출제의도를 만족하게 풀이하였다. python으로 코테를 푸는 이상 2차원 배열에 종속되어 문제를 
풀어나가는 행위자체가 감점 요소이며, 3가지 showing case에서 어떤 형식으로 조건문 분리를 할지 명확하게
보여주어야 했다고 본다.

def solution(array):
    while len(array) != 0:
        for i, a in enumerate(set(array)):
            array.remove(a)
        if i == 0: return a
    return -1
    
2번 출제의도 문제이다. for loop의 iterator가 loop이 끝난 후에도 상태를 유지하고 있음을 알고 있어야
쉽게 접근할 수 있지 않았나 싶다. 
'''
