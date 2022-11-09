def solution(s):
    stack = []
    for i in range(len(s)):
        temp = s[i]
        if stack and stack[-1] == temp:
            stack.pop()
        else:
            stack.append(temp)
    
    if stack: 
        return 0
    else: 
        return 1