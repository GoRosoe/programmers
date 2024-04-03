def solution(myString, pat):
    answer = ""
    if myString[::-1].find(pat[::-1]) == 0:
        answer = myString
    else:
        answer = myString[ : - myString[::-1].find(pat[::-1])]
    return answer