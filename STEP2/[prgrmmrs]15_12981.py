# https://programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words): 
    idx = 0 
    aset = set() 
    aset.add(words[0]) 

    for i in range(1, len(words)): 
        prev, cur = words[i-1], words[i] 
        if prev[-1] != cur[0] or cur in aset: 
            idx = i 
            break 
        aset.add(cur) 

    if idx == 0: return [0, 0] 
    return [idx%n+1, idx//n+1] 