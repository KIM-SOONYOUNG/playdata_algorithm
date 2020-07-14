# https://programmers.co.kr/learn/courses/30/lessons/12906
def solution(arr):
    answer = [arr[0]]
    for elem in arr: 
        if elem != answer[-1]: answer.append(elem)
    return answer