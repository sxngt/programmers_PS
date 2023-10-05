def solution(n):
    nbin = bin(n)[2:]
    while True:
        if nbin.count('1') == bin(n+1)[2:].count('1'):
            break
        else:
            n += 1
    return n+1


print(solution(78))