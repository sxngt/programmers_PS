def task(count, num: str, zero):
    count += 1
    a = num.count('1')
    res = len(num) - a
    num = bin(int(a))[2:]
    zero += res
    if num == '1':
        #print(count, num, zero)
        return count, num, zero
    #print(count, num, zero)
    return task(count, num, zero)


def solution(s: str):
    return [task(0, s, 0)[0], task(0, s, 0)[2]]


print(solution("110010101001"))
