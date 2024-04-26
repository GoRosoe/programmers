def solution(my_string):
    answer = []
    number = "1234567890"
    for i, n in enumerate(my_string):
        if n in number:
            answer.append(int(n))
    return sorted(answer)