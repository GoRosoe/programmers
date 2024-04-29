def solution(n):
    number = [1,2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    result = 0
    for i in range(1, n+1):
        if i not in number:
            result += 1
    return result