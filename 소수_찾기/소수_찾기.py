from math import sqrt
from itertools import permutations
def isPrime(a):
    if(a < 2):
        return False
    for i in range(2,int(sqrt(a))+1):
        if(a % i == 0):
            return False
    return True

def solution(numbers):
    cnt = 0
    ans = []
    ans2 = []
    for i in range(len(numbers),0,-1):
        ans.append(list(permutations(sorted(list(numbers)),i)))
    for i in ans:
        for j in i:
            ans2.append(int("".join(j)))
    for i in set(ans2):
        if isPrime(i):
            cnt += 1
    return cnt

print(solution("011"))
