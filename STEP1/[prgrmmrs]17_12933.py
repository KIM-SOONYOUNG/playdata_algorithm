def solution(n):
    return int(''.join(list(map(str, sorted(list(map(int, str(n))), reverse=True)))))