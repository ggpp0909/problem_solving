def solution(str1, str2):
    str1 = str1.upper()  # 대문자로 다 통일
    str2 = str2.upper()

    # 알파벳만 골라서 글자 두개씩 묶기
    set1 = list()
    set2 = list()
    for i in range(len(str1) - 1):
        if 65 <= ord(str1[i]) <= 90 and 65 <= ord(str1[i + 1]) <= 90:
            set1.append(str1[i] + str1[i + 1])
    for i in range(len(str2) - 1):
        if 65 <= ord(str2[i]) <= 90 and 65 <= ord(str2[i + 1]) <= 90:
            set2.append(str2[i] + str2[i + 1])

    visited = {}

    inter = 0
    for i in range(len(set1)):
        if visited.get(set1[i], 1):
            visited[set1[i]] = 0
            inter += min(set1.count(set1[i]), set2.count(set1[i])) # 중복원소 -> 개수 작은거 교집합 더해주기

    tot = len(set2) + len(set1) - inter
    if tot == 0:
        return 65536
    ans = int((inter / tot) * 65536)
    return ans

solution('handshake', 'shake hands	')