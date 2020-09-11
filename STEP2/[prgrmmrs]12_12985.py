# https://programmers.co.kr/learn/courses/30/lessons/12985


def solution(n, a, b):
    answer = 0 

    alist = [i for i in range(1, n+1)] 

    while len(alist): 
        tmp = list() 
        for i in range(0, len(alist), 2): 
            cur = alist[i:i+2]
            if a in cur and b in cur: return answer + 1
            
            if a in cur: tmp.append(a) 
            elif b in cur: tmp.append(b) 
            else: tmp.append(alist[i]) 
        answer += 1
        alist = tmp 

    return answer