def solution(my_string, is_prefix):
    answer = 0
    result = ""
    for i in my_string:
        result += i
        if result == is_prefix:
            answer = 1
    return answer