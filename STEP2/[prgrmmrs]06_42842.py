# https://programmers.co.kr/learn/courses/30/lessons/42842


import math
def solution(brown, red):
    answer = []

    total_area = brown + red
    root = int(round(math.sqrt(total_area), 0))
    for a in range(root, brown):
        b = int((brown/2) - a + 2)  # 2(a+b) - 4 = brown
        if a >= b and b > 0:
            if a * b == total_area:
                return [a, b]
    return answer