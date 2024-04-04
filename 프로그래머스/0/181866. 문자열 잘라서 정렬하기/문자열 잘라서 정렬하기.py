def solution(myString):
    result = []
    sorted_list = sorted(myString.split("x"))
    for i in sorted_list:
        if i == "":
            continue
        else:
            result.append(i)
    return result