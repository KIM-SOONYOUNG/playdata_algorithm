def solution(arr1, arr2):
    m, n = len(arr1), len(arr1[0]) 
    answer = [[0]*n for _ in range(m)] 
    for i in range(m): 
        for j in range(n): answer[i][j] = arr1[i][j] + arr2[i][j]
    return answer