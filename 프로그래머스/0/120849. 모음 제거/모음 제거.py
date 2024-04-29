def solution(my_string):
    answer = ''
    a = "aeiou"
    for i, n in enumerate(my_string):
        if n not in a:
            answer += n
    return answer