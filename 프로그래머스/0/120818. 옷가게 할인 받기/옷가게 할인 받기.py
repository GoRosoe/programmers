def solution(price):
    if price < 100000:
        return price
    elif 100000 <= price < 300000:
        return price * 95 // 100
    elif 300000 <= price < 500000:
        return price * 90 // 100
    else:
        return price * 80 // 100