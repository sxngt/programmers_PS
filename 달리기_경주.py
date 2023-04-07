players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]
a,b = dict(),dict()
for i, j in enumerate(players):
    a[i] = j
    b[j] = i
print(a,b)

for call in callings:
    before = a[b[call]-1]

    b[before] += 1
    b[call] -= 1
    a[b[before]] = before
    a[b[call]] = call

answer = sorted(b,key = lambda x:b[x])

print(answer)
