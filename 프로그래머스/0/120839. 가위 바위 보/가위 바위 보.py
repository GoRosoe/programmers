def solution(rsp):
    answer = ''
    for i, n in enumerate(rsp):
        if n == "2":
            answer += "0"
        elif n == "0":
            answer += "5"
        else:
            answer += "2"
    return answer