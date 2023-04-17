def solution(genres: list, plays: list[int]):
    cnt = dict()
    cnt2 = dict()
    answer = []
    for i, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in cnt:
            cnt[genre] = [[play,i]]
        else:
            cnt[genre].append([play, i])
    for k, v in cnt.items():
        cnt2[sum(list(map(lambda x: x[0], v)))] = k

    for i in sorted(cnt2.keys())[::-1]:
        tmp = cnt[cnt2[i]]
        tmp.sort(key=lambda x: x[0])
        tmp.reverse()
        if len(tmp) != 1:
            tmp = tmp[0:2]
            if tmp[0][0] == tmp[1][0]:
                tmp.sort(key=lambda x:x[1])

        tmp2 = []
        for j in tmp:
            tmp2.append(j[1])
        answer.append(tmp2)
    return sum(answer, []), cnt, cnt2

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
