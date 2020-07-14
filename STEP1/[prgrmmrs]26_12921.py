# Not solved 
prime = [2]

for i in range(3, 1000001, 2): 
    if i % 2 == 0: continue
    check = True 
    for elem in prime: 
        if elem > i//2: break 
        if i % elem == 0: 
            check = False 
            break 
    if check: prime.append(i) 

def solution(n):
    answer = 0
    for idx, elem in enumerate(prime): 
        if elem <= n: return idx + 1