# https://programmers.co.kr/learn/courses/30/lessons/12913

def solution(land):
    answer = 0
    n, m = len(land), len(land[0]) 
    dp_arr = [[0]*m for _ in range(n)] 
    for i in range(m): dp_arr[0][i] = land[0][i] 

    for i in range(1, n): 
        for j in range(m): 
            maximum = 0 
            for k in range(m): 
                if j == k: continue 
                maximum = max(maximum, dp_arr[i-1][k]) 
            dp_arr[i][j] = maximum + land[i][j] 

    return max(dp_arr[-1])