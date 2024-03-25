def solution(num_list):
    answer = 0
    for i, e in enumerate(num_list):
        while e != 1:
            if e % 2 == 0:
                e = e // 2
            else:
                e = (e-1) // 2
            answer += 1
    return answer