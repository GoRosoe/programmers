def solution(my_string):
    result = ""
    for i in range(len(my_string)):
        if my_string[i] not in result:
            result += my_string[i]
    return result