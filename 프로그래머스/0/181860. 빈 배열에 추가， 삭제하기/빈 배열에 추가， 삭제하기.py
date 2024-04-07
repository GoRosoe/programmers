def solution(arr, flag):
    answer = []
    for i, e in enumerate(flag):
        if e == True:
            for j in range(2 * arr[i]):
                answer.append(arr[i])
        else:
            for j in range(arr[i]):
                answer.pop() * arr[i]
    return answer