# https://programmers.co.kr/learn/courses/30/lessons/12940
def gcd(a, b): 
    while b: 
        tmp = a % b
        a = b 
        b = tmp 
    return a

def solution(n, m):
    n, m = max(n, m), min(n, m) 
    return [gcd(n, m), int(n*m/gcd(n, m))]