def solution(x, n):
    answer = []
    interval = x
    for i in range(n): 
        answer.append(x) 
        x += interval
    return answer