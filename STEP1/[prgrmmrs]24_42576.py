def solution(participant, completion):
    adict = dict() 
    for elem in participant: 
        if elem not in adict: adict[elem] = 1
        else: adict[elem] += 1
    
    for elem in completion: adict[elem] -= 1
    for elem in adict: 
        if adict[elem] != 0: return elem
