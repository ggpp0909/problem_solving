score = []
for _ in range(10): #입력 10개 받기
    a=int(input())
    score.append((a))

stack=0
stack_lst=[]
a_lst=[]

for i in score:
    stack += i
    stack_lst.append(stack)
    a=abs(stack - 100)
    a_lst.append(a)

stack_lst=stack_lst[::-1]  #뒤
a_lst=a_lst[::-1]

print(stack_lst[a_lst.index(min(a_lst))])





    

