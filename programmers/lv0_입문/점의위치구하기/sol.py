def solution(dot):
    if dot[0] > 0 and dot[1] > 0:
        return 1
    if dot[0] < 0 and dot[1] > 0:
        return 2
    if dot[0] < 0 and dot[1] < 0:
        return 3
    else:
        return 4


print(solution([2, 4]))
print(solution([-7, 9]))