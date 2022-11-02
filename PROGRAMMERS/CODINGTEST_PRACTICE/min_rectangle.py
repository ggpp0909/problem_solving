def solution(sizes):
    # 가로랑 세로의 길이를 늘리면서 탐색할거야
    # 지금 보고있는명함이 가로랑 세로 길이 내에 있다? 그럼 굳이 회전시켜서 볼 필요도없어 continue
    # 만약 삐져나온다? 그러면 지금 가로세로상태랑, 가로 세로 바꾼상태중 뭐가 더 이득인지를 보고 지갑 크기를 늘려야돼
    
    w = sizes[0][0]
    h = sizes[0][1]
    
    for i in range(len(sizes)):
        card_w, card_h = sizes[i][0], sizes[i][1]
        if card_w <= w and card_h <= h:
            continue
        else:
            rotate_w, rotate_h = card_h, card_w
            # 원래꺼 삐져나온거, 회전시켜서 삐져나온것중 덜 차이나는 쪽으로 지갑 크기 늘리기
            temp = max(0, card_w - w) + max(0, card_h - h)
            temp2 = max(0, rotate_w - w) + max(0, rotate_h - h)
            if temp <= temp2:
                w += max(0, card_w - w)
                h += max(0, card_h - h)
            else:
                w += max(0, rotate_w - w)
                h += max(0, rotate_h - h)
                
    ans = w * h
    return ans