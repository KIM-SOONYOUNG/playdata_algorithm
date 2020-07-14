def solution(s):
    if len(s) not in [4, 6]: return False 
    num_list = list(map(str, [i for i in range(10)]))
    for elem in s:
        if elem not in num_list: return False 
    return True 