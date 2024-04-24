def solution(i, j, k):
    num_list = ""
    for i in range(i, j+1):
        num_list += str(i)
    return num_list.count(str(k))