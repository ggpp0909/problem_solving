p , w = map(int,input().split())
key=[" ","ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
string=input()
str_to_num=[]
clk=0

for i in range(len(string)):
    for k in range(len(key)):
        if string[i] in key[k]:
            clk= clk + key[k].index(string[i]) #같은 숫자일때 몇번 더누르냐
            str_to_num.append(k) #문자에 해당하는 숫자 저장

#print(str_to_num)

diff_num_cnt = 0
same_num_cnt = 0

for i in range(len(str_to_num)-1):
    if str_to_num[i] == str_to_num[i+1]: #기준숫자와 다음숫자가 같을경우
        if str_to_num[i] == 0: #공백인경우
            clk += 1
        else:
            same_num_cnt +=1
    else:
        diff_num_cnt += 1

tot= same_num_cnt * w + p * (same_num_cnt+diff_num_cnt+clk+1) # +1은 마지막 숫자 누를경우
print(tot)
