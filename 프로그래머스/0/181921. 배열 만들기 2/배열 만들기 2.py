def solution(l, r):
    answer = []
    for i in range(l, r+1):
        num = ""
        for j in str(i):
            if j == "5" or j == "0":
               num += j
        if str(i) == num:
            answer.append(i)
    if answer == []:
        answer.append(-1)    
    return answer
