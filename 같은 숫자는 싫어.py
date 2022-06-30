def solution(arr):
    answer = []
    for i in range(len(arr)-1):
        if arr[i]!=arr[i+1]:
            answer.append(arr[i])
        if len(arr)-2 == i:
            answer.append(arr[i+1])
            
    return answer