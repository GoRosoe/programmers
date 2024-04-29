def solution(balls, share):
    answer1 = 1
    answer2 = 1
    for i in range(balls - share + 1, balls+1):
        answer1 *= i
    for i in range(1, share+1):
        answer2 *= i    
    return answer1 // answer2