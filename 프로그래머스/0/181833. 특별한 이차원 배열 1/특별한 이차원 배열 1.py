import numpy as np

def solution(n):
    answer = np.zeros((n,n))
    for i in range(n):
        answer[i][i] = 1
    return answer.tolist()
