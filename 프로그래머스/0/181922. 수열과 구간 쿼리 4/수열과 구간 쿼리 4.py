def solution(arr, queries):
    for i in range(len(arr)):
        for s, e, k in queries:
            if s <= i <= e and i%k == 0:
                print(i, k)
                arr[i] += 1
    return arr 