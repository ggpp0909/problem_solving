def solution(n, t, m, timetable):   # 운행횟수, 운행간격, 한번에 태울사람수, 사람들도착시간
    # 대기순서대로 세운다? -> 큐 ?
    # 우선 timetable을 분으로 환산
    time = [] # deque는 sort가 안되더라
    for i in timetable:
        time.append(min_convert(i))
    # 오름차순정렬
    time.sort()
    # print(time)
    start_time = 540    # 출발시간은 9시 -> 540분
    bus_arr = [[] for i in range(n)]    # 버스 운행 하는 횟수에 맞춰서 배열에 탑승시킨다
    idx = 0             # time 배열에서 가리킬 인덱스
    while idx < n:
        inbus = 0
        while inbus < m:
            if time:
                if time[0] <= start_time:
                    bus_arr[idx].append(time.pop(0))
            inbus += 1
        idx += 1
        start_time += t
    # print(bus_arr)

    # 마지막 버스가 다 차있다면?
    if len(bus_arr[-1]) == m:
        temp = bus_arr[-1][-1]   # 마지막 사람 끌어내고 내가 타
        ans = temp - 1
    else:  # 막차에 빈공간이 있다면
        ans = start_time - t    # 막차타 ( start_time에 막차시간 들어가있음 )

    ans_h = str(ans // 60)
    ans_m = str(ans % 60)
    if len(ans_h) == 1:
        ans_h = '0' + ans_h
    if len(ans_m) == 1:
        ans_m = '0' + ans_m

    answer = ans_h + ':' + ans_m
    # print(answer)
    return answer


def min_convert(time):  # time = "HH:MM"
    hour = int(time[0:2])
    min = int(time[3:5])
    convert = hour * 60 + min
    return convert

solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"])
solution(2, 10, 2, ["09:10", "09:09", "08:00"])
solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"])
solution(10, 60, 45, ["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"])