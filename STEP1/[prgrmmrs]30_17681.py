# https://programmers.co.kr/learn/courses/30/lessons/17681
def to_bin(num, n): 
    res = '' 
    n -= 1 

    while n > -1: 
        cur = 2**n
        if num >= cur: 
            res += '1' 
            num -= cur
        else: res += '0' 
        n -= 1
    return res
    

def solution(n, arr1, arr2):
    answer = []
    arr1 = [to_bin(elem, n) for elem in arr1] 
    arr2 = [to_bin(elem, n) for elem in arr2] 

    for i in range(n): 
        tmp = '' 
        for j in range(n): 
            if arr1[i][j] == '1' or arr2[i][j] == '1': tmp += '#' 
            else: tmp += ' ' 
        answer.append(tmp) 

    return answer 