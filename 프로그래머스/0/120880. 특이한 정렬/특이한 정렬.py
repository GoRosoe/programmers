def solution(numlist, n):
    result = []
    num = 0
    while len(numlist) != len(result):
        if n in numlist:
            result.append(n)
        num += 1
        if num % 2 == 1:
            n += num
        else:
            n -= num
    return result