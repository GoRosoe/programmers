def solution(picture, k):
    answer = []
    line = ""
    for i, e in enumerate(picture):
        for j in range(len(e)):
            line += e[j] * k
        for _ in range(k):
            answer.append(line)
        line = ""
    return answer