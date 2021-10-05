import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    length = int(input())
    string = input()
    stack = []
    res = ''
    for x in string:
        if x.isdecimal():   # 숫자면 일단 꺼내
            res += x
        else:
            if x == '(':        # 여는괄호 만나면 stack에 append
                stack.append(x)
            elif x == '*' or x == '/':
                while stack and (stack[-1] == '*' or stack[-1] == '/'):     # 곱하기 나누기 보다 우선순위가 낮은애들 나올때까지 res에 더함
                    res += stack.pop()
                stack.append(x)
            elif x == '+' or x == '-':      # + - 보다 우선순위가 낮은애는 (밖에 없으니 그거전까지 꺼내서 더함
                while stack and stack[-1] != '(':
                    res += stack.pop()
                stack.append(x)
            elif x == ')':
                while stack and stack[-1] != '(':
                    res += stack.pop()  # 닫는괄호 만나면 여는괄호 만나기 전까지 스택에서 pop해서 res에 더함
                stack.pop()
    while stack:        # stack에 남아있는 연산자 모두 꺼내서 더함
        res += stack.pop()

    stack2 = []
    for x in res:
        if x not in '+*':
            stack2.append(x)
        elif x == '+':
            b = int(stack2.pop())
            a = int(stack2.pop())
            stack2.append(a+b)
        elif x == '*':
            b = int(stack2.pop())
            a = int(stack2.pop())
            stack2.append(a*b)
    print('#{} {}'.format(tc, stack2[0]))

# 장하석의 코드를 참고하였음