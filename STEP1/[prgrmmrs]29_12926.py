# https://programmers.co.kr/learn/courses/30/lessons/12926
def solution(s, n):
    answer = ''
    small = [ord('a'), ord('z')] 
    large = [ord('A'), ord('Z')] 

    for elem in s: 
        if elem == ' ': answer += elem 
        else: 
            cur = ord(elem) 
            if small[0] <= cur <= small[1]: 
                cur += n 
                if cur > small[1]: cur = small[0] + (cur - small[1] - 1) 
            else: 
                cur += n 
                if cur > large[1]: cur = large[0] + (cur - large[1] - 1)
            answer += chr(cur) 
    return answer