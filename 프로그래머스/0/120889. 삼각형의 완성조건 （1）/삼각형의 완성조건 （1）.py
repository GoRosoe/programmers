def solution(sides):
    if sorted(sides)[0] + sorted(sides)[1] > max(sides):
        return 1
    else:
        return 2
