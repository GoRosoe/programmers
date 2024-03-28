def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs:
        number = int(i[s:s+l])
        if k < number: answer.append(number)
    return answer