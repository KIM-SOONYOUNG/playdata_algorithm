# https://programmers.co.kr/learn/courses/30/lessons/12953
def gcd(a, b): 
    while b: 
        tmp = a % b
        a = b 
        b = tmp 
    return a

def lcd(a, b): 
    g = gcd(a, b) 
    return int(a * b / g) 
    
def solution(arr):
    if len(arr) == 1: return arr[0] 

    arr.sort() 
    answer = arr[0] 
    for elem in arr[1:]: 
        answer = lcd(answer, elem) 
    return answer 
