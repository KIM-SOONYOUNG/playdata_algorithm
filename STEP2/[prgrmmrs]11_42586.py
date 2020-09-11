# https://programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    answer = [] 

    days = list() 
    for p, s in zip(progresses, speeds): 
        rest = 100 - p 
        if rest % s > 0: days.append(rest//s+1) 
        else: days.append(rest//s)
    
    current, tmp = days[0], 0
    for day in days: 
        if current < day: 
            answer.append(tmp) 
            current = day 
            tmp = 1
        else: tmp += 1
            
    answer.append(tmp) 
    return answer



# def solution(progresses, speeds):
#     answer = []

#     length = len(progresses)
#     rest_days = [0 for _ in range(length)]
    
#     for i in range(length):
#         rest_work = 100 - progresses[i]
#         speed = speeds[i]
#         rest_work = rest_work//speed if rest_work % speeds[i] == 0 else rest_work//speed + 1
#         rest_days[i] = rest_work

#     cnt, i = 0, 0
#     big_rest = rest_days[i]

#     while i < length:
#         target = rest_days[i]
        
#         if target <= big_rest:
#             cnt += 1
#             i += 1
#         else:
#             answer.append(cnt)
#             cnt = 0
#             big_rest = rest_days[i]
#     answer.append(cnt)
#     return answer