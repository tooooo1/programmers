def solution(id_list, report, k):
    #한 번에 한 명의 유저 신고
    report = set(report)
    
    # 신고 임시 저장 (유저ID: 유저가 신고한 ID)
    arrayReport = {}
    for i in report:
        name = i.split()
        if name[0] in arrayReport:
            arrayReport[name[0]]+=[name[1]]
        else:
            arrayReport[name[0]]=[name[1]]
            
    print(arrayReport)
    
    # 신고 받은 인원들 => tempReport
    tempReport = []
    for i in arrayReport.values():
        tempReport +=i
    
    # K만큼 신고 확인
    reportK = []
    for i in id_list:
        if i in tempReport:
            if tempReport.count(i) >= k:
                reportK += [i]
    
    # 메일 전송
    answer = []
    for i in id_list:
        if i in arrayReport.keys():
            count = 0
            for j in arrayReport[i]:
                if j in reportK:
                    count +=1
            answer += [count]
        else:
            answer += [0]
        
    return answer