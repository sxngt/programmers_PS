s = "    3people unFollowed    3A  a    23asd 123 asd    me "
test = 0
answer = []
ls = list(map(str, s.split(' ')))
print(ls)

for i in ls:
    try:
        test = int(i[0])
        answer.append(i[0]+i[1:].lower())
    except:
        if i == "":
            answer.append("")
        else:
            answer.append(i[0].upper()+i[1:].lower())


print(" ".join(answer))

