# 풀이1
def solution(str1, str2):
    return 1 if str2 in str1 else 2

# 풀이2
def solution(str1, str2):
    if str2 in str1:
        answer = 1
    else:
        answer = 2
    return answer

print(solution("ab6CDE443fgh22iJKlmn1o", "6CD"))
print(solution("ppprrrogrammers", "pppp"))
print(solution("AbcAbcA", "AAA"))