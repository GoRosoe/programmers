def solution(quiz):
    answer = []
    result = 0
    for i in quiz:
        if i.split(" ")[1] == "+":
            result = int(i.split(" ")[0]) + int(i.split(" ")[2])
        else:
            result = int(i.split(" ")[0]) - int(i.split(" ")[2])
        if result == int(i.split(" ")[-1]):
            answer.append("O")
        else:
            answer.append("X")
    return answer