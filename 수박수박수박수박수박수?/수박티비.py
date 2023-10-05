a = ""
n = 99999
for i in range(1, n+1):
    if i % 2 != 0:
        a += "수"
    else:
        a += "박"

print(a)