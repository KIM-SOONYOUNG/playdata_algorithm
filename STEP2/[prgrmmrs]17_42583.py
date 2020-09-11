# https://programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque 

def solution(bridge_length, weight, truck_weights):
    
    answer = 0
    queue = deque() 
    truck_weights = truck_weights[::-1]
    
    time = 1 
    total_weight = 0 
    while truck_weights: 

        if not queue: 
            elem = truck_weights.pop()
            total_weight += elem
            queue.append((elem, time))
        else: 
            if queue[0][1] + bridge_length == time: 
                elem, _ = queue.popleft() 
                total_weight -= elem 
            
            if total_weight + truck_weights[-1] <= weight: 
                elem = truck_weights.pop() 
                total_weight += elem 
                queue.append((elem, time)) 

        time += 1

    time -= 1
    return bridge_length + time
