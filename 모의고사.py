def solution(answers):
    #수포자가 찍는 방식
    student = [[1, 2, 3, 4, 5], # 1번
               [2, 1, 2, 3, 2, 4, 2, 5], # 2번
               [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # 3번
              ]
    
    #수포자의 정답 개수
    ans = []
    for k in range(len(student)):
        count = 0
        for i in range(len(answers)):
            if answers[i] == student[k][i%len(student[k])]:
                count+=1
        ans.append(count)

    #가장 많이 맞춘 수포자
    result = []
    for i in range(len(ans)):
        if ans[i] == max(ans):
            result.append(i+1)

    return result