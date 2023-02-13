import heapq

N = int(input())
info_dict = dict()
ans = 0
for _ in range(N):
    input_temp = input().split()

    if input_temp[0] == "1":
        name = input_temp[1]
        if info_dict.get(name): # 이미 있으면
            temp = info_dict[name]
            for i in input_temp[3:]:
                heapq.heappush(temp, -int(i))
            info_dict[name] = temp
        else:
            temp = []
            for i in input_temp[3:]:
                heapq.heappush(temp, -int(i))
            info_dict[name] = temp
    else:
        name = input_temp[1]
        n = int(input_temp[2])
        if not info_dict.get(name):
            continue
        temp = info_dict[name]
        for i in range(n):
            if len(temp) == 0: break
            ans -= heapq.heappop(temp)
        info_dict[name] = temp

print(ans)
