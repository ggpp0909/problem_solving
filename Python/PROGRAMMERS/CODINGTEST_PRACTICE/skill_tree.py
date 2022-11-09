def solution(skill, skill_trees):
    answer = -1
    ans = 0
    for i in skill_trees:
        stack = []
        for j in i:
            if j not in skill:
                continue
            stack.append(j)
            
        index = 0
        for j in range(len(stack)):
            if skill[j] != stack[j]:
                break
        else:
            ans += 1         
        
    return ans