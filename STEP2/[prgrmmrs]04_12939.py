# https://programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
    alist = list(map(int, s.split())) 
    alist.sort() 

    return ' '.join(list(map(str, [alist[0], alist[-1]])))
