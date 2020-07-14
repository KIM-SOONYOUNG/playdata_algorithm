def solution(answers):
    adict = dict() 
    adict[1] = [1, 2, 3, 4, 5]
    adict[2] = [2, 1, 2, 3, 2, 4, 2, 5]
    adict[3] = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    cnt = dict() 
    for i in range(1, 4): 
        cnt[i] = 0 
        k = 0 
        for elem in answers: 
            if adict[i][k] == elem: cnt[i] += 1 
            k += 1 
            if k == len(adict[i]): k = 0 

    cnt = [elem for elem in cnt.items()]
    cnt.sort(key=lambda x:x[1], reverse=True) 
    
    res = [cnt[0]] 
    for elem, n in cnt[1:]: 
        if res[-1][1] == n: res.append((elem, n)) 
        else: break 
    return [elem for elem, _ in res]