# https://programmers.co.kr/learn/courses/30/lessons/12922
def solution(n):
    answer = ''
    answer += '수박'*(n//2) 
    answer = answer + '수' if n%2 == 1 else answer 
    return answer