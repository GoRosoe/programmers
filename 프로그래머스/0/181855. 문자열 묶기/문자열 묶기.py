def solution(strArr):
    answer = []
    for i in strArr:
        answer.append(len(i))
    return answer.count(max(set(answer), key=answer.count))