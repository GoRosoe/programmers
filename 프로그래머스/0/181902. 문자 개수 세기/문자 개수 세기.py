def solution(my_string):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    answer = [0] * 52
    for i in range(len(my_string)):
        for j in range(52):
            if my_string[i] == alphabet[j]:
                answer[j] += 1
    return answer