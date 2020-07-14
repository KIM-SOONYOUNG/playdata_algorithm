# https://programmers.co.kr/learn/courses/30/lessons/12910
def solution(arr, divisor):
    answer = [elem for elem in arr if elem%divisor == 0]
    if answer: return sorted(answer)
    else: return [-1]