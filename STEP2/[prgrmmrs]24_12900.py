# https://programmers.co.kr/learn/courses/30/lessons/12900

def solution(n):
    MOD = 1000000007 

    dp_arr = [0]*(n+1) 
    dp_arr[1] = 1 
    dp_arr[2] = 2 

    for i in range(3, n+1): 
        dp_arr[i] = dp_arr[i-1] + dp_arr[i-2] 
        dp_arr[i] %= MOD 

    return dp_arr[n]