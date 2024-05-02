def solution(my_string, n):
    answer = ""
    for i, m in enumerate(my_string):
        answer += n * m
    return answer