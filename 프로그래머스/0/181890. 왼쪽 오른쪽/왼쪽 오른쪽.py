def solution(str_list):
    answer = []
    if "r" in str_list and "l" in str_list: 
        if str_list.index("r") < str_list.index("l"):
            answer = str_list[str_list.index("r") + 1 :]
        else:
            answer = str_list[ : str_list.index("l")]
            
    if "r" not in str_list and "l" in str_list: 
        answer = str_list[ : str_list.index("l")]
    
    if "l" not in str_list and "r" in str_list:
        answer = str_list[str_list.index("r") + 1 :]
        
    return answer