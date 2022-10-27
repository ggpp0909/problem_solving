
T = int(input())

# (ZERO) ONE (TWO) (THREE) (FOUR) (FIVE) (SIX) (SEVEN) (EIGHT) NINE
# 알파벳 개수로 찾으면 될거같은데
#  X가 있으면 6 -> S가 있으면 7, W가 있으면 2, G가 있으면 8 -> H가 있으면 3 (Z가 있으면 0), -> R이 있으면 4 -> F가 있으면 5, O가 있으면 1, 그담 9


for k in range(T):
    word = input()
    alpha = {}
    for i in range(26):
        alpha[chr(ord("A") + i)] = 0
    
    for i in word:
        alpha[i] += 1
    
    ans = []
    
    # 6찾기
    ans += [6] * alpha["X"]
    alpha["S"] -= alpha["X"]
    alpha["I"] -= alpha["X"]
    alpha["X"] = 0

    # 7찾기
    ans += [7] * alpha["S"]
    alpha["E"] -= 2 * alpha["S"]
    alpha["V"] -= alpha["S"]
    alpha["N"] -= alpha["S"]
    alpha["S"] = 0

    # 2찾기
    ans += [2] * alpha["W"]
    alpha["T"] -= alpha["W"]
    alpha["O"] -= alpha["W"]
    alpha["W"] = 0

    # 8찾기
    ans += [8] * alpha["G"]
    alpha["E"] -= alpha["G"]
    alpha["I"] -= alpha["G"]
    alpha["H"] -= alpha["G"]
    alpha["T"] -= alpha["G"]
    alpha["G"] = 0

    # 3찾기
    ans += [3] * alpha["H"]
    alpha["T"] -= alpha["H"]
    alpha["R"] -= alpha["H"]
    alpha["E"] -= 2 * alpha["H"]
    alpha["H"] = 0

    # 0찾기
    ans += [0] * alpha["Z"]
    alpha["E"] -= alpha["Z"]
    alpha["R"] -= alpha["Z"]
    alpha["O"] -= alpha["Z"]
    alpha["Z"] = 0

    # 4찾기
    ans += [4] * alpha["R"]
    alpha["F"] -= alpha["R"]
    alpha["O"] -= alpha["R"]
    alpha["U"] -= alpha["R"]
    alpha["R"] = 0

    # 5찾기
    ans += [5] * alpha["F"]
    alpha["I"] -= alpha["F"]
    alpha["V"] -= alpha["F"]
    alpha["E"] -= alpha["F"]
    alpha["F"] = 0

    # 1찾기
    ans += [1] * alpha["O"]
    alpha["N"] -= alpha["O"]
    alpha["E"] -= alpha["O"]
    alpha["O"] = 0
    
    # 9찾기
    ans += [9] * (alpha["N"] // 2)


    ans = "".join(map(str, sorted(ans)))
    print("Case #{}: {}".format(k + 1, ans))

