def solution(myStr):
    result = []
    answer = ""
    for i in range(len(myStr)):
        if myStr[i] != "a" and myStr[i] != "b" and myStr[i] != "c":
            answer += myStr[i]
        elif answer != "":
            result.append(answer)
            answer = ""
    result.append(answer)
    if answer == "":
        result = ["EMPTY"]
    return result