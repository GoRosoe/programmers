def solution(array, n):
    count = 0
    while True:
        if n - count in array:
            answer = n - count
            break     
        elif n + count in array:
            answer = n + count            
            break
        else:
            count += 1
    return answer