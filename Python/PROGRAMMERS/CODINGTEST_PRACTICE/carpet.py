def solution(brown, yellow):
    size = brown + yellow
    
    # size의 약수쌍 구하기
    div = []
    for i in range(1, size + 1):
        if i * i > size: #약수는 쌍으로 존재하므로 반만
            break
        
        if size % i == 0:
            div.append([size // i, i]) 
            # 가로길이가 더 기므로 순서 이렇게
    # print(div)
    
    for i in div:
        x, y = i
        if (x - 2) * (y - 2) == yellow:
            return i
        


# solution(10, 2)
# solution(8, 1)
# solution(24, 24)