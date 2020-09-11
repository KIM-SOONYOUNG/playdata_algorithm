# https://programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    aset = set(nums) 

    return max(len(aset), len(nums)//2)