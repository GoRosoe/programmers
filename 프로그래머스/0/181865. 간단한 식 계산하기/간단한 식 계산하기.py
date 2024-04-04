def solution(binomial):
    num_list = binomial.split(" ")
    if num_list[1] == "+":
        result = int(num_list[0]) + int(num_list[2])
    elif num_list[1] == "-":
        result = int(num_list[0]) - int(num_list[2])
    else:
        result = int(num_list[0]) * int(num_list[2])
    return result