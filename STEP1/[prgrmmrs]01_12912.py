# https://programmers.co.kr/learn/courses/30/lessons/12912
def solution(a, b):
    return sum([i for i in range(min(a, b), max(a, b)+1)])