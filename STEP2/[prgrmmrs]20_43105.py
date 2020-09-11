# https://programmers.co.kr/learn/courses/30/lessons/43105

def solution(triangle):

    for i in range(1, len(triangle)): 
        n = len(triangle[i])

        triangle[i][0] += triangle[i-1][0] 
        triangle[i][n-1] += triangle[i-1][n-2] 

        for j in range(1, n-1):
            triangle[i][j] += max(triangle[i-1][j-1:j+1]) 

    return max(triangle[-1])