def solution(num_list):
    mul = 1
    total = 0
    for i in num_list:
        mul *= i
        total += i
    if mul > (total**2):
        answer = 0
    else:
        answer = 1
    return answer