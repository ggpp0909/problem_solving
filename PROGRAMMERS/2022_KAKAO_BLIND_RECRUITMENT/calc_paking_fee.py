import math


def convert_time(time):
    return int(time[0:2]) * 60 + int(time[-2:])


def solution(fees, records):
    base_time = fees[0]
    base_fee = fees[1]
    unit_time = fees[2]
    unit_fee = fees[3]

    parked_at = [0 for i in range(10000)]  # 언제 주차했는지
    # parked_at 만 쓰려했더니 00:00일때 예외처리 힘듬
    is_parking = [False for i in range(10000)]
    total_time = [0 for i in range(10000)]  # 총 이용시간

    for i in range(len(records)):
        temp = records[i].split(" ")
        time, car_num, is_enter = temp

        car_num = int(car_num)
        time = convert_time(time)

        if is_enter == "OUT":  # 전날 입차한 차까지 처리 가능
            total_time[car_num] += time - parked_at[car_num]
            parked_at[car_num] = 0
            is_parking[car_num] = False
        else:
            parked_at[car_num] = time
            is_parking[car_num] = True

    # 마지막까지 출차 안한 차 처리
    for i in range(len(parked_at)):
        if is_parking[i]:
            total_time[i] += (23 * 60 + 59) - parked_at[i]

    ans = []
    for i in range(len(total_time)):
        if total_time[i]:
            # 조건1 기본시간 이하라면 기본요금 청구
            if total_time[i] <= base_time:
                ans.append(base_fee)
            else:
                fee = base_fee + \
                    math.ceil(
                        (total_time[i] - base_time) / unit_time) * unit_fee
                ans.append(fee)

    return ans
