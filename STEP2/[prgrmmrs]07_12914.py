# https://programmers.co.kr/learn/courses/30/lessons/12914

def solution(n):
    dp_arr = [0] * (2001) 

    dp_arr[1] = 1
    dp_arr[2] = 2 
    if n <= 2: return dp_arr[n] 

    for i in range(3, n+1): 
        dp_arr[i] = dp_arr[i-1] + dp_arr[i-2] 
        dp_arr[i] %= 1234567

    return dp_arr[n]