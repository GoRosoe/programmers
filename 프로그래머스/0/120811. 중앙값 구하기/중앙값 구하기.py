def solution(array):
    
    return sorted(array)[len(array)/2] if len(array) % 2 == 0 else sorted(array)[int(len(array)/2)]