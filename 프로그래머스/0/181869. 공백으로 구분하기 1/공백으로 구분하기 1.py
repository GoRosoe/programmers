def solution(my_string):
    answer = []
    a = ""
    for i in my_string:
        if i != " ":
            a += i
        else:
            answer.append(a)
            a = ""
    answer.append(a)
    return answer