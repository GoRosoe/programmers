def solution(n):
    count = 1
    answer = 1
    while n >= answer:
        count += 1
        answer *= count 
    return count - 1