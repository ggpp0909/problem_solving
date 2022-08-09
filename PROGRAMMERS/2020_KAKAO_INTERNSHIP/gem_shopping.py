
# 정확성 통과, 효율성 0점...
def solution(gems):
    kind = len(set(gems)) # 보석 종류수
    
    for i in range(kind, len(gems) + 1):
        s = 0
        e = i - 1 # 슬라이딩 윈도우의 포인터 정의
        
        # 첫 윈도우 생성 and check
        purchase = {}
        for j in range(0, i):
            if gems[j] in purchase:
                purchase[gems[j]] += 1
            else:
                purchase[gems[j]] = 1
        
        if len(purchase) == kind:
            return [1, i]
        
        # 슬라이딩
        while e < len(gems) - 1:
            # s 포인터 이동
            purchase[gems[s]] -= 1
            if purchase[gems[s]] == 0:
                del purchase[gems[s]]
            s += 1
            
            # e 포인터 이동
            e += 1
            if gems[e] in purchase:
                purchase[gems[e]] += 1
            else:
                purchase[gems[e]] = 1
            
            # check
            if len(purchase) == kind:
                return [s + 1, e + 1]