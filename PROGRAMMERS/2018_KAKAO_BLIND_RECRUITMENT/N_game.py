def solution(n, t, m, p): # 진수, 말해야되는횟수, 참가인원, 내 순서
    answer = ''     # 여기에 쌓을거야
    number = "0123456789ABCDEF"
    st = '0'

    num = 1
    while len(st) < t * m:  # 참가인원 * 내가 말해야되는 횟수 만큼 넉넉하게 st에 담는다
        x = num
        s = ''
        while x > 0:
            s += str(number[x % n])     # n진수이므로 number에서 index 슬라이싱
            x //= n                     # 만약 num이 45, 16진수라면 s에 D3 이 쌓임, 거꾸로하면 3D => 45
        st += s[::-1]
        num += 1
    print(st)

    idx = p - 1 # p번째 숫자 말하기, answer에 답이 t개만큼 쌓일때 까지
    while len(answer) < t:
        answer += st[idx]
        idx += m

    return answer

solution(16, 16, 2, 2)