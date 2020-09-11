# https://programmers.co.kr/learn/courses/30/lessons/49993

def solution(skill, skill_trees):
    answer = 0

    adict = dict() 
    for idx, char in enumerate(skill): adict[char] = idx 

    for elem in skill_trees: 
        alist = [adict[char] for char in elem if char in adict]

        check = True 
        for idx, s in enumerate(alist): 
            if idx != s: 
                check = False 
                break 
        if check: answer += 1


    return answer 