def solution(nums):
    setNums = set(nums)
    
    if len(setNums) < len(nums)/2:
        return len(setNums)
    else:
        return int(len(nums)/2)