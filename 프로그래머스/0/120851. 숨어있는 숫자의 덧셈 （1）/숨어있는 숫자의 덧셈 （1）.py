def solution(my_string):
    answer = 0
    number = "1234567890"
    for i, n in enumerate(my_string):
        if n in number:
            answer += int(n)
    return answer