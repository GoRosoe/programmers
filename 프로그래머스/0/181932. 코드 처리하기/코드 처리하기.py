def solution(code):
    ret = ""
    a = 0
    b = 1
    for i in range(0, len(code)):
        if code[i] == "1":
            a, b = b, a
            continue
        if i % 2 == a:
            ret += code[i]
    if ret == "":
        ret = "EMPTY"
    return ret
            
    
    