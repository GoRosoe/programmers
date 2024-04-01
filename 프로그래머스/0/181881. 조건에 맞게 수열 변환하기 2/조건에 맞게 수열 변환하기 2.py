def solution(arr):
    arr2 = []
    count = 0
    while True:
        arr2 = arr.copy()
        for i, e in enumerate(arr):
            if e % 2 == 0 and e >= 50:
                arr[i] = arr[i] // 2
            elif e % 2 == 1 and e < 50:
                arr[i] = 2 * arr[i] + 1
        if  arr2 == arr:
            break
        count += 1
    return count