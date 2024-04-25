def solution(s):
    s_list = s.split(" ")
    answer = 0
    for i, n in enumerate(s_list):
        if n == "Z":
            answer -= int(s_list[i-1])
        else:
            answer += int(n)                
    return answer