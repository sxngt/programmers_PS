def solution(food):
    answer = ''
    for i, foo in enumerate(food):
        if foo%2 == 1:
            foo -= 1
        answer += str(i+1)*(foo//2)
    return answer

print(solution())


