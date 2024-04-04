def solution(myString, pat):
    result = ""
    for i in range(len(myString)):
        if myString[i] == "A":
            result += "B"
        else:
            result += "A"
    return int(pat in result)