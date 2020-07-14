# https://programmers.co.kr/learn/courses/30/lessons/12921

def solution(n):

    answer = 0

    check = [False]*(n+1) 
    for i in range(2, n+1): 
        if check[i]: continue 
        check[i] = True 
        answer += 1
        for j in range(i+i, n+1, i): 
            check[j] = True 
    return answer


