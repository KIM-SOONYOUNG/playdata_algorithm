# https://programmers.co.kr/learn/courses/30/lessons/42861

from collections import deque 

def solution(n, costs):
    answer = 0

    costs.sort(key=lambda x:x[2], reverse=True)

    arr = [[False]*n for _ in range(n)] 

    def cnt_partial(arr): 
        check = [False]*n 
        ret = 0 
        
        def dfs(node): 
            check[node] = True 
            for i in range(n): 
                if not check[i] and arr[node][i]: dfs(i) 
            
        for i in range(n): 
            if not check[i]: 
                ret += 1
                dfs(i) 

        return ret 

    check = [1]*n
    while costs: 
        if sum(check) == 0 and cnt_partial(arr) == 1: break 

        x, y, c = costs.pop() 
        if check[x] + check[y] == 0:
            tmp_cnt = cnt_partial(arr) 
            arr[x][y] = arr[y][x] = True 
            if tmp_cnt > cnt_partial(arr): answer += c
            else: arr[x][y] = arr[y][x] = False 
            continue

        check[x] = check[y] = 0        
        arr[x][y] = arr[y][x] = True 
        answer += c 

    return answer