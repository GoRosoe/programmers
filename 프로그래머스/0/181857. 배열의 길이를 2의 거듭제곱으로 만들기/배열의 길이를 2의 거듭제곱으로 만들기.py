def solution(arr):
    i = 1
    while True:
        if len(arr) == 1:
            break
        elif 2**i >= len(arr):
            for _ in range((2**i - len(arr))):
                arr.append(0)
            break
        else:
            i += 1
    return arr