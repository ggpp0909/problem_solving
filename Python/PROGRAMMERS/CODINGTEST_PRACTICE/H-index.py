def solution(citations):
    citations.sort()
    ans = 0
    for i in range(len(citations)):
        if citations[i] >= len(citations) - i:
            return len(citations) - i
    return ans