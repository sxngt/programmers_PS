def solution(sizes):
    w, h = [], []
    for rec in sizes:
        w.append(max(rec))
        rec.remove(max(rec))
        h.append(rec[0])
    return max(w)*max(h)


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
