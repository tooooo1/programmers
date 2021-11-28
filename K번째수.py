def solution(array,commands):
    answer = []
    for i in commands:
        start, end, sequence = i
        temp = array[start-1:end]
        temp.sort()
        answer.append(temp[sequence-1])

    return answer