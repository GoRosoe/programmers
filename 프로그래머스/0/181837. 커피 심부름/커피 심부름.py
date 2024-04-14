def solution(order):
    money = 0
    for i in order:
        if i == "anything" or "americano" in i:
            money += 4500
        else:
            money += 5000    
    return money