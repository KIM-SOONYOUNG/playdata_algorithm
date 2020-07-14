# https://programmers.co.kr/learn/courses/30/lessons/12933
def solution(n):
    return int(''.join(list(map(str, sorted(list(map(int, str(n))), reverse=True)))))