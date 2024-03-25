def solution(ineq, eq, n, m):
    if ineq == ">" and eq == "!":
        result = n > m     
    elif ineq == ">" and eq == "=":
        result = n >= m
    elif ineq == "<" and eq == "=":
        result = n <= m
    else:
        result = n < m    
    if result:
        result = 1
    else:
        result = 0
    return result