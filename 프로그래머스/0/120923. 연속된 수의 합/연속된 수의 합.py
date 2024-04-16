def solution(num, total):        
    answer = []
    num_fac = 0
    for i in range(1, num):
        num_fac += i
    
    x = (total - num_fac) // num
    
    for i in range(x, x+num):
        answer.append(i)
        
    return answer