import sys
sys.stdin = open('input.txt')

n = int(input())
for k in range(1, n + 1):
    eq = input().split()

    # 후위 -> 계산
    ans_stack = []
    for i in range(len(eq)):
        try:
            if eq[i] == '.':
                if len(eq[i:]) != 1 or len(ans_stack) != 1:
                    ans_stack = ['error']
                break
            if eq[i] in '*/-+':
                x = ans_stack.pop()
                y = ans_stack.pop()
                if eq[i] == '*':
                        ans_stack.append(x * y)
                elif eq[i] == '/':
                        ans_stack.append(y // x)
                elif eq[i] == '-':
                        ans_stack.append(y - x)
                elif eq[i] == '+':
                        ans_stack.append(x + y)
            else:
                ans_stack.append(int(eq[i]))
        except:
            ans_stack = ['error']

    print('#{} {}'.format(k, ans_stack.pop()))
