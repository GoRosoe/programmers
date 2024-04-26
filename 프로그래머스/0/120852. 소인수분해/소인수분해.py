def solution(n):
    answer = []
    count = 2
    while n != 1:
        if n % count == 0:
            answer.append(count)
            n = n // count
        else:
            count += 1
    return sorted(list(set(answer)))