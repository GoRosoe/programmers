def solution(num_list):
    odd = even = 0
    for i in range(len(num_list)):
        if i % 2 == 1:
            odd += num_list[i]
        else:
            even += num_list[i]
    return odd if odd > even else even