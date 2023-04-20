def solution(brown, yellow):
    ans = []
    ans2 = []

    for i in range(1, yellow + 1):
        y = yellow / i
        if y == int(y):
           ans.append([int(y), i])
    for i in ans:
        ans2.append(abs(i[0] - i[1]))

    tmp = ans[ans2.index(min(ans2))]
    return [tmp[0]+2, tmp[1]+2]

print(solution(10, 2))


