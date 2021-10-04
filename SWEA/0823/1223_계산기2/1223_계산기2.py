import sys
sys.stdin = open('input.txt')

for k in range(1, 11):
    n = int(input())
    eq = input()

    # 후위표기식으로 변경
    stack_temp = []
    stack = []
    for i in eq:
        if i == '*':
            stack_temp.append(i)
        elif i == '+':
            stack += stack_temp[::-1]
            stack_temp = []
            stack_temp.append(i)
        else:
            stack.append(i)
    stack = stack + stack_temp[::-1]

    # 후위 -> 계산
    ans_stack = []
    for i in stack:
        if i == '*':
            x = ans_stack.pop()
            y = ans_stack.pop()
            ans_stack.append(x * y)
        elif i == '+':
            x = ans_stack.pop()
            y = ans_stack.pop()
            ans_stack.append(x + y)
        else:
            ans_stack.append(int(i))

    print('#{} {}'.format(k, ans_stack.pop()))

