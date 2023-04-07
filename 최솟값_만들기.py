a = [1, 4, 2]
b = [5, 4, 4]
sum = 0
for i,j in zip(sorted(a),sorted(b)[::-1]):
    sum += i*j

print(sum)
