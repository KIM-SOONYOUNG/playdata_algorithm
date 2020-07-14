# https://programmers.co.kr/learn/courses/30/lessons/12934
from math import sqrt 
def solution(n):
    answer = 0
    MAX = 50000000000000
    for i in range(1, int(sqrt(MAX))): 
        if i * i == n: return (i+1)**2 
        if i * i > n: return -1 