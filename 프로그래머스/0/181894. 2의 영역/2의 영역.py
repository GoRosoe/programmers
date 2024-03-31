def solution(arr):
    answer = []
    for i in range(len(arr)):
        if arr[i] == 2:
            answer.append(i)
    if answer == []:
        answer = [-1]
    else:
        answer = arr[answer[0] : answer[-1]+1]
    return answer