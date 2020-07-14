# https://programmers.co.kr/learn/courses/30/lessons/42862
def solution(n, lost, reserve):
    answer = 0 
    lost, reserve = set(lost) - set(reserve), set(reserve) - set(lost)
    for elem in lost: 
        if elem-1 in reserve: 
            reserve.remove(elem-1) 
            answer += 1
        elif elem+1 in reserve: 
            reserve.remove(elem+1) 
            answer += 1
    return answer + n - len(lost)