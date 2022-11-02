def solution(progresses, speeds):
    progresses = progresses[::-1]
    speeds = speeds[::-1]
    ans = []
    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        
        if progresses[-1] >= 100:
            cnt = 0
            while progresses and progresses[-1] >= 100:
                progresses.pop()
                cnt += 1
            ans.append(cnt)
        
    return ans