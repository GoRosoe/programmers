def solution(A, B):
    count = 0
    while True:
        if A == B:
            break
        elif B == A[-1] + A[:len(A)-1]:
            count +=  1
            break
        elif count == len(A):
            count = -1
            break
        else:
            A = A[-1] + A[:len(A)-1]
            count += 1
            
    return count