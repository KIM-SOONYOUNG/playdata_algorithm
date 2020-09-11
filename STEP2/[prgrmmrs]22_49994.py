# https://programmers.co.kr/learn/courses/30/lessons/49994

def solution(dirs):
    answer = 0

    dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
    astring = 'URDL' 
    adict = dict() 
    for idx, char in enumerate(astring): adict[char] = idx 

    n = 5 
    x, y = n, n
    
    check = set() 

    for elem in dirs:
        k = adict[elem]  
        nx, ny = x+dx[k], y+dy[k] 
        if 0 <= nx < 2*n+1 and 0 <= ny < 2*n+1: 
            tmp_tuple = tuple([x, y, nx, ny]) 
            tmp_tuple2 = tuple([nx, ny, x, y]) 
            if tmp_tuple not in check and tmp_tuple not in check: 
                check.add(tmp_tuple) 
                check.add(tmp_tuple2)
                answer += 1 

            x, y = nx, ny 

    return answer