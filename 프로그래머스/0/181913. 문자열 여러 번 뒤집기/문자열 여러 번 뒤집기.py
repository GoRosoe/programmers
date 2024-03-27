def solution(my_string, queries):
    my_string_list = list(my_string)
    for i, j in queries:
        while i < j:
            my_string_list[i], my_string_list[j] = my_string_list[j] , my_string_list[i]
            i += 1
            j -= 1
    return ''.join(my_string_list)