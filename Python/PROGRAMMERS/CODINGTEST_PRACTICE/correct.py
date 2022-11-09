def solution(s):
    stack = [s[0]]
    
    for i in range(1, len(s)):
        if s[i] == "(":
            stack.append(s[i])
        else:
            if not stack:
                return False
            elif stack[-1] == "(":
                stack.pop()
            else:
                return False
            
    if stack:
        return False
    
    return True