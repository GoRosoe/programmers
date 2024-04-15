def solution(arr):
    diff_arr = len(arr[0]) - len(arr)
    
    # 열의 개수가 더 많을 때
    if diff_arr > 0:
        for _ in range(diff_arr):
            arr.append( [0] * len(arr[0]))  
    # 행의 개수가 더 많을 때
    elif diff_arr < 0:
         for i in range(len(arr)):
            for _ in range(-diff_arr):
                arr[i].append(0)
    return arr