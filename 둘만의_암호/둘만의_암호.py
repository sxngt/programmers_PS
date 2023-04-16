import string

s = "aukks"
skip = "wbqd"
index = 5
res = []
res2 = []
answer = ""
abc = []
a = dict()
b = dict()
for i in string.ascii_lowercase:
    if i not in skip:
        abc.append(i)
for i, j in enumerate(abc):
    a[i+1] = j
    b[j] = i+1

for i in s:
    res.append(b[i])
g = len(a)
for i in res:
    if i+index > g:
        res2.append((i+index) % g)
    else:
        res2.append(i+index)


for i in res2:
    answer += a[i]

print(answer)
print(res, res2, g, index)
print(a,b)





