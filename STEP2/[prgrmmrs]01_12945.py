# https://programmers.co.kr/learn/courses/30/lessons/12945
def solution(n):

    dp_arr = [0]*(n+1) 

    dp_arr[1] = 1 

    for i in range(2, n+1): 
        dp_arr[i] = dp_arr[i-1] + dp_arr[i-2] 
    return dp_arr[n] 

    
