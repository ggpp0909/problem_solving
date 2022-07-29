# def solution(user_id, banned_id):
#     answer = 0
#     arr = [[] for i in range(len(banned_id))]
    
#     # arr 의 banned_id인덱스에 가능한 user_id후보 인덱스를 저장
#     for i in range(len(user_id)):
#         for j in range(len(banned_id)):
#             if len(user_id[i]) != len(banned_id[j]): # 길이 다르면 비교할 필요없음
#                 continue
#             idx = 0
#             flag = True
            
#             while idx < len(user_id[i]):
#                 if banned_id[j][idx] == "*": # *은 걍넘어가
#                     idx += 1
#                     continue
#                 else:
#                     if user_id[i][idx] != banned_id[j][idx]: # 같은 인덱스의 문자가 다르면 후보제외
#                         flag = False
#                         break
#                     else:
#                         idx += 1

#             # while 끝까지 통과하면 후보 추가
#             if flag:
#                 arr[j].append(i)
#     print(arr)
    
#     # 4번 템플릿으로 뻗어나가 보기
#     # banned_id를 순회할건데 매치 된 user_id는 visit처리하기
#     ans_arr = [0 for i in range(1 << len(user_id))]
#     ans = 0
#     def recur(cur, cnt, visit, visit2):
#         nonlocal ans
#         if cnt == len(banned_id): # 뽑은 횟수가 banned_id와 같으면
#             # print("visit", visit)
#             if not ans_arr[visit]:
#                 ans_arr[visit] += 1
#                 # print(ans_arr)
#                 # print(bin(visit))
#             return
        
#         if cur == len(banned_id): #cur번째 
#             return
        
#         # visit -> user_id, visit2 -> banned_id, 매칭했을경우 둘다 visit처리하기
#         recur(cur + 1, cnt, visit, visit2) # 안뽑을 경우
#         for i in range(len(arr)): # arr의 원소들 별로 뽑냐 안뽑냐, 뽑을경우 누굴뽑냐
#             for j in range(len(arr[i])):
#                 if visit & (1 << arr[i][j]) or visit2 & (1 << i):
#                     continue               
#                 recur(cur + 1, cnt + 1, visit | (1 << arr[i][j]), visit2 | (1 << i))
#     recur(0, 0, 0, 0)
#     # print(sum(ans_arr))

#     return sum(ans_arr)

########

def is_collect(a, b): # a와 b가 일치할 가능성이 있는지 여부 반환, b가 banned_id
    if len(a) != len(b):
        return False
    idx = 0
    while idx < len(a):
        if a[idx] == b[idx] or b[idx] == "*":
            idx += 1
        else:
            return False
    return True

def solution(user_id, banned_id):
    # 1.banned_id의 길이와 같은 user_id 순열 만들기
    # 2.무지성 비교
    
    visited = [False for i in range(len(user_id))]
    can = []
    arr = []
    def recur(cur):
        if cur == len(banned_id):
            can.append(arr[:])
            return
        
        for i in range(len(user_id)):
            if visited[i]:
                continue
            visited[i] = True
            arr.append(user_id[i])
            recur(cur + 1)
            arr.pop()
            visited[i] = False
    recur(0)
    ans = []
    for i in range(len(can)):
        idx = 0
        flag = True
        while idx < len(banned_id):
            if not is_collect(can[i][idx], banned_id[idx]):
                flag = False
                break
            idx += 1
        if flag:
            temp = sorted(can[i])
            if temp in ans:
                continue
            ans.append(temp)
    # print(len(ans))
    return len(ans)