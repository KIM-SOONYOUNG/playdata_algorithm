# https://programmers.co.kr/learn/courses/30/lessons/42898

def solution(m, n, puddles):

    MOD = 1000000007 
    dp_arr = [[0]*m for _ in range(n)] 

    for x, y in puddles: dp_arr[y-1][x-1] = -1 
    
    for i in range(1, m): 
        if dp_arr[0][i] != -1: dp_arr[0][i] = 1
        else: break 

    for i in range(1, n): 
        if dp_arr[i][0] != -1: dp_arr[i][0] = 1
        else: break 



    for i in range(1, n): 
        for j in range(1, m): 
            if dp_arr[i][j] == -1: continue 

            left, up = dp_arr[i-1][j], dp_arr[i][j-1] 
            dp_arr[i][j] = max(left, 0) + max(up, 0) 
            dp_arr[i][j] %= MOD

    
    return dp_arr[-1][-1] 

