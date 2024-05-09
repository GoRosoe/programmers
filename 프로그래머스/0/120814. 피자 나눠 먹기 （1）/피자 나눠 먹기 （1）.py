def solution(n):
    count = 1
    while True:
        if count * 7 >= n:
            return count
        else:
            count += 1