def solution(rank, attendance):
    attendance_list = []
    for i, e in enumerate(attendance):
        if e == True:
            attendance_list.append([rank[i], i])
    sort_list = sorted(attendance_list)
    return (sort_list[0][1] * 10000) + (sort_list[1][1] * 100) + (sort_list[2][1])
    