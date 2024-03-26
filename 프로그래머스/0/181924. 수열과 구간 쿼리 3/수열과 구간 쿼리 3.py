def solution(arr, queries):
    answer = arr
    for i in queries:
        res1 = arr[i[0]]
        res2 = arr[i[1]]
        answer[i[0]] = res2
        answer[i[1]] = res1
    return answer