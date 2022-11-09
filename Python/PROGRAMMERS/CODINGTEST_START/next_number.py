def solution(common):
    # 이놈이 등차인지 등비인지 알아내는 무언가가 필요
    # 등차 or 등비일때 그 공차 or 공비 ? 구하고
    # 그걸 그 수열에 맞춰서 다음거에 적용을 하면 되겠지
    # 파이썬은 1초에 1억의 연산
    
    flag = True # 트루일때 등차, 폴스일때 등비
    temp = common[1] - common[0] # 공차
    for i in range(1, len(common)):
        if common[i] != common[i - 1] + temp:
            flag = False
            temp = common[1] / common[0]
            break

    ans = 0
    if flag: # 등차 수열 일 경우
        ans = common[-1] + temp
    else:
        ans = common[-1] * temp
        
    return ans