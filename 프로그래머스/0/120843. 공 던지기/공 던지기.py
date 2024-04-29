def solution(numbers, k):
    return (numbers * (((2* k) // len(numbers)) + 1))[(2*k)-2]