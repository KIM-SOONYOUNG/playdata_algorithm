# Not solved 
def solution(n):
    answer = 0
    prime = [2] 

    for i in range(3, n+1): 
        if i % 2 == 0: continue
        check = True 
        for elem in prime: 
            if elem > i//2: break 
            if i % elem == 0: 
                check = False 
                break 
        if check: prime.append(i) 
    return len(prime)