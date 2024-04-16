def solution(babbling):
    saying = ["aya", "ye", "woo", "ma"]
    answer = 0
    for i in range(len(babbling)):
        for j in saying:
            babbling[i] = babbling[i].replace(j, " ")
        print(babbling[i])
        if babbling[i].strip() == "":
                answer += 1
    return answer