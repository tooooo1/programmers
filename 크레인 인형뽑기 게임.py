def solution(board, moves):
    basket = [] #담을 바구니 배열
    count = 0 #지운 개수
    
    #크레인 이동
    for i in moves:
        for j in range(len(board)):
            # 인형을 만나면 바구니에 넣기
            if board[j][i-1]:
                basket.append(board[j][i-1])
                board[j][i-1] = 0
                break
        
        #바구니에 값이 있다면 같은 것이 있는지 확인
        if len(basket)>1:
            # 같은 인형이 있다면 제거 후 count
            if basket[-1]==basket[-2]:
                count+=2
                del basket[-1]
                del basket[-1]
            
    return count