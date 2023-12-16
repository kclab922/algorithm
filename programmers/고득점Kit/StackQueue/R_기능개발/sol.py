from collections import deque

def solution(pro, spd):
    answer = []

    fin = deque()
    for p, s in zip(pro, spd):
        fin.append((100-p)//s+1 if (100-p)%s else (100-p)//s)
    # fin = deque([7, 3, 9])

    temp = [9] 
    temp.append(fin.popleft())
    while len(fin):
        if temp[0] >= fin[0]:
            temp.append(fin.popleft())
        else:
            answer.append(len(temp))
            temp = [fin.popleft()]

    answer.append(len(temp)) # 2 1
    
    return answer


print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
