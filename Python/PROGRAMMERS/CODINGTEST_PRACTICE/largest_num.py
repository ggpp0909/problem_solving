def three_digit(num):
    if len(str(num)) == 1: # 3이면  3333으로 리턴
        return int(str(num) * 4)
    elif len(str(num)) == 2: # 34면 3434으로 리턴
        return int(str(num) * 2)
    elif len(str(num)) == 3: # 345면 3453로 리턴
        return int(str(num) + str(num)[0])
    elif len(str(num)) == 4:
        return 1000


def solution(numbers:list):
    numbers.sort(key=lambda x: three_digit(x), reverse=True)
    ans = ''
    for i in numbers:
        ans += str(i)

    return str(int(ans))
