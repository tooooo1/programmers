def pos(left, right, num, hand):
    #키패드 좌표 설정
    keypad = {
        1:(0,0), 2:(0,1), 3:(0,2),
        4:(1,0), 5:(1,1), 6:(1,2),
        7:(2,0), 8:(2,1), 9:(2,2),
        '*':(3,0), 0:(3,1), '#':(3,2)
    }
    
    #거리 계산
    distLeft = abs(keypad[num][0] - keypad[left][0]) + abs(keypad[num][1] - keypad[left][1])
    distRight = abs(keypad[num][0] - keypad[right][0]) + abs(keypad[num][1] - keypad[right][1])
    
    #거리 비교
    if distLeft < distRight:
        return 'L'
    elif distLeft > distRight:
        return 'R'
    else:
        #거리가 같다면 어느 손잡이인지 판별
        if hand=='right':
            return 'R'
        else:
            return 'L'

def solution(numbers, hand):
    #손 세팅
    leftHand = [1,4,7]
    rightHand = [3,6,9]
    middle = [2,5,8,0]
    
    #초기값 세팅
    answer = ''
    left = '*'
    right = '#'
    
    
    for i in numbers:
        #왼손이면
        if i in leftHand:
            answer+='L'
            left = i
            
        #오른손이면
        if i in rightHand:
            answer+='R'
            right = i
            
        #중간이면
        if i in middle:
            answer+=pos(left, right, i, hand)
            #손 위치 세팅
            if pos(left, right, i, hand) == 'L':
                left = i
            else:
                right = i
            
    return answer