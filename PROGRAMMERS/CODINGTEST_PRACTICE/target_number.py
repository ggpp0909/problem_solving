def solution(numbers, target):
    def recur(cur, calc):
        if cur == len(numbers):
            if calc == target:
                return 1
            return 0
        return recur(cur + 1, calc + numbers[cur]) + recur(cur + 1, calc - numbers[cur])
    
    # print(ans)
    answer = recur(0, 0)
    # print(answer)
    return answer


# solution([1, 1, 1, 1, 1], 3)