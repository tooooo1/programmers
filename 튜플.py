def solution(s):
    tempList = []
    count = 0
    flag = False
    for i in range(1, len(s)-1):
        if flag:
            count+=1
            
        if s[i] == "{":
            flag = True
        if s[i] == "}":
            flag = False
            changeList = list(map(int,s[i-count+1:i].split(',')))
            tempList.append((count,changeList))
            count = 0
    tempList.sort()
    
    answer = []
    for t in tempList:
        x, y = t
        for state in y:
            if state not in answer:
                answer.append(state)
    
    return answer