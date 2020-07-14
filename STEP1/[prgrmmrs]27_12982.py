# https://programmers.co.kr/learn/courses/30/lessons/12982
def solution(d, budget):
    answer = 0

    d.sort() 
    for elem in d: 
        if elem <= budget: 
            budget -= elem 
            answer += 1
        else: break 
    return answer 