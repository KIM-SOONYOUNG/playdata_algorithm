# https://programmers.co.kr/learn/courses/30/lessons/12919
def solution(seoul):
    answer = '김서방은 {loc}에 있다'
    for idx, elem in enumerate(seoul): 
        if elem == "Kim": return answer.format(loc=idx)
