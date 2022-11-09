# def solution(expression):
#     # 기호 분리
#     mark = []
#     num = []
#     temp = ''
#
#     for i in expression:
#         if not i.isdigit():
#             mark.append(i)
#             num.append(temp)
#             temp = ''
#         else:
#             temp += i
#     num.append(temp)    #마지막은 부호 안만나므로 그냥 append
#     print(mark)
#     print(num)
#
#     answer = 0
#     return answer
#

# expression 길이 3이상 100이하, 순서재정의가 아니라 연산자 우선순위 재정의, 연산자는 무조건 3개

def calc(a, b, op):
    if op == '-':
        return int(a) - int(b)
    if op == '+':
        return int(a) + int(b)
    if op == '*':
        return int(a) * int(b)


def solution(expression):
    # visited = [False for i in range(3)]
    # mark = []
    # temp = ['*', '+', '-']
    # arr = []
    # ans = 0
    # def recur(cur):
    #     if cur == 3:
    #         # print(mark)
    #         arr.append(mark[:])
    #         return
    #
    #     for i in range(3):
    #         if visited[i]:
    #             continue
    #         visited[i] = True
    #         mark.append(temp[i])
    #         recur(cur + 1)
    #         mark.pop()
    #         visited[i] = False
    # recur(0)
    # print(arr)
    mark = [['*', '+', '-'], ['*', '-', '+'], ['+', '*', '-'], ['+', '-', '*'], ['-', '*', '+'], ['-', '+', '*']]
    sep = [] # expresstion의 숫자와 연산자를 분리한 배열
    temp = ''
    for i in expression:
        if not i.isdigit():
            sep.append(temp)
            temp = ''
            sep.append(i)
        else:
            temp += i
    sep.append(temp)
    # print(sep)
    ans = 0
    for i in range(6):
        temp = sep[:] # 뒤에서부터 연산할거야
        temp.reverse()
        for j in mark[i]: # 연산자 우선순위 순회

            for k in range(len(temp) - 2, 0, -2): # 연산자는 1번인덱스부터 2칸간격으로 있음 끝에서부터 pop하면서 업데이트
                if temp[k] == j: # 연산자를 만난다면 앞뒤를 연산
                    temp[k - 1] = calc(temp[k + 1], temp[k - 1], j)
                    del temp[k:k+2]

        ans = max(ans, abs(int(temp[0])))
            # print(temp)
    # print(ans)
    # print(sep)
    return ans

solution("100-200*300-500+20")
solution("50*6-3*2")
solution("200-300-500-600*40+500+500")
solution("1-1")