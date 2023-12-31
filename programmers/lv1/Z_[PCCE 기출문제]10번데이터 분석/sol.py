def solution(data, ext, v_ext, srt):
    answer = []
    mdict = {"code":0, "date":1, "maximum":2, "remain":3}
    
    for d in data:
        if d[mdict[ext]] < v_ext:
            answer.append(d)

    return sorted(answer, key = lambda x: x[mdict[srt]])

print(solution([[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]], "date", 20300501, "remain"))