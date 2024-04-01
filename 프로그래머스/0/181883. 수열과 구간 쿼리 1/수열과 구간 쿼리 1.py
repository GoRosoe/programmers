def solution(arr, queries):
    for i, j in queries:
        for k in range(len(arr)):
            if i <= k <= j:
                arr[k] += 1
    return arr