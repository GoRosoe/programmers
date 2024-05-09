def solution(n):
    count = 1
    while True:
        if count * 6 % n == 0:
            return count
        else:
            count += 1