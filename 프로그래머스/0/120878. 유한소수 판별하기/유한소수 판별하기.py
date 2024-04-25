def solution(a, b):
    # 유한소수가 되기 위한 분수의 조건
    # - 기약분수로 나타내었을 때, 분모의 소인수가 2와 5만 존재
    gcd = 0
    # a와 b의 공약수로 b를 나눔.
    for i in range(1, b):
        if a % i == 0 and b % i == 0:
            gcd = i
    b = b // gcd
    
    while b % 2 == 0 or b % 5 == 0:
        if b % 2 == 0:
            b = b // 2 
        else:
            b = b // 5 
    return 1 if b == 1 else 2