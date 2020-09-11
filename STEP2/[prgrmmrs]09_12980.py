# https://programmers.co.kr/learn/courses/30/lessons/12980

def solution(n):
    answer = 0 

    while n: 
        if n % 2 == 0:  n //= 2 
        else: 
            n -= 1 
            answer += 1
    return answer