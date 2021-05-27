s=input()
s=s.upper() #대문자변환
s_uniq=set(s) #세트(집합) 중복값 없음, 순서없음 -> 중복값제거용
s_uniq=list(s_uniq)
a=[]
for i in range(len(s_uniq)):
    a.append(s.count(s_uniq[i])) #a에 알파벳의 중복수 저장
if a.count(max(a))>1: #최대값이 여러개면
    print("?")
else:
    print(s_uniq[a.index(max(a))]) #한개라면
