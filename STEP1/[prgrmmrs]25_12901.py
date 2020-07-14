def solution(a, b):
    day_list = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    tot = 4
    for i in range(1, a): 
        if i % 2 == 0: 
            if i == 2: tot += 29 
            elif i in [8, 10]: tot += 31 
            else: tot += 30

        else: 
            if i in [9, 11]: tot += 30 
            else: tot += 31 
            
    tot += b 
    return day_list[tot%7]
