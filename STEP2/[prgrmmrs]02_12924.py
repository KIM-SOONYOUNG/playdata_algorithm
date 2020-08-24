# https://programmers.co.kr/learn/courses/30/lessons/12924

def solution(n):
    answer = 0

    for i in range(1, n+1): 
        tmp = 0 
        for k in range(i, n+1): 
            tmp += k 
            if tmp >= n: 
                if tmp == n: answer += 1
                break 
            

    return answer
    
