def solution(given):
#     n = len(given)
#     divide = []
#     for i in range(1, n + 1):
#         if i * i > n:   
#             break        

#         if n % i == 0:
#             divide.append(i)
#             if i * i != n:
#                 divide.append(n // i)
#     # print(divide)
    ans = len(given)
    
    for i in range(1, len(given)//2 + 10): # 최대길이 절반
        s = i
        cnt = 1
        word = given[:i]
        comp = ""
        # print(word)
        while s <= len(given):
            nxt = given[s:s + i]
            if word == nxt:
                cnt += 1
            else:
                if cnt > 1:
                    comp += str(cnt) + word
                else:
                    comp += word
                word = nxt
                cnt = 1
            s += i
        if s > len(given): # 범위초과해서 생략된거 있으면 뒤에 다 붙이기
            comp += given[s - i:]
        # print(comp)
        ans = min(ans, len(comp))
    return ans