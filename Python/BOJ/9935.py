word = input()
boom = list(input())

trigger = boom[-1]
stack = []

for i in range(len(word)):
    stack.append(word[i])
    if word[i] == trigger:
        if stack[-len(boom):] == boom:
            for j in range(len(boom)):
                stack.pop()

if stack:
    print(*stack, sep='')
else:
    print('FRULA')