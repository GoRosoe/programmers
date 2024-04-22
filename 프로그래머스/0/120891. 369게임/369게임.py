def solution(order):
    result = 0
    for i in range(len(str(order))):
        if int(str(order)[i]) % 3 == 0 and str(order)[i] != "0":
            result += 1
    return result