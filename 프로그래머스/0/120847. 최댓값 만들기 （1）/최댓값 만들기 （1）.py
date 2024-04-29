def solution(numbers):
    answer = sorted(numbers)[-2: ]
    return answer[0] * answer [1]