from itertools import combinations

def solution(places):
    answer = []
    for place in places:
        people = []
        for x in range(5):
            for y in range(5):
                if place[x][y] == "P":
                    people.append((x,y))
        
        #사람이 없거나 혼자 있을 때는 거리두기 O
        if len(people)<2:
            answer+=[1]
            continue
        
        #조합하여 맨해튼 거리 계산 (1, 2일 때만 고려)
        flag = False
        combPeople = list(combinations(people, 2))
        for p in combPeople:
            x, y = p
            r1, c1 = x
            r2, c2 = y
            
            #1이면 무조건 거리두기 X (바로 옆자리)
            if abs(r1-r2)+abs(c1-c2) == 1:
                answer+=[0]
                break
            
            #2이면 옆과 대각 비교
            if abs(r1-r2)+abs(c1-c2) == 2:
                #c는 다르고, 같은 r일 때
                if not abs(r1-r2):
                    if place[r1][max(c1,c2)-1] != "X":
                        answer+=[0]
                        flag = True
                        break
                    
                #r은 다르고, 같은 c일 때
                if not abs(c1-c2):
                    if place[max(r1,r2)-1][c1] != "X":
                        answer+=[0]
                        flag = True
                        break
                
                #대각선일 때
                if abs(r1-r2) == 1:
                    if place[r1][c2] != "X" or place[r2][c1] != "X":
                        answer+=[0]
                        flag = True
                        break
        
        if not flag:
            answer+=[1]
            flag = False
    return answer
            
        