# https://programmers.co.kr/learn/courses/30/lessons/12938

def solution(n, s):

    if n > s: return [-1] 

    if s % n == 0: return [s//n]*n

    k = s // n 
    res = s % n 
    answer = [k]*n 
    for i in range(1, res+1): 
        answer[-i] += 1
    return answer 