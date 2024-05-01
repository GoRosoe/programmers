def solution(age):
    answer = ""
    alphabet = 'abcdefghij'
    for i in range(len(str(age))):
        answer += alphabet[int(str(age)[i])]
    return answer