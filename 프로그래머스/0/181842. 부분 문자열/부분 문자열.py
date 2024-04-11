def solution(str1, str2):
    answer = 1
    if str2.find(str1) == -1:
        answer = 0
    return answer