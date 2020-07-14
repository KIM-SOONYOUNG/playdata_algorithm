def solution(s):
    i = len(s) 
    return s[i//2] if i%2 == 1 else s[i//2-1:i//2+1]