word=input()
key=[2,3,4,5,6,7,8,9]
alpha=["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
tot=0
for i in range(len(word)):
    for j in range(len(alpha)):
        if word[i] in alpha[j]:
            location=alpha.index(alpha[j])
            temp=key[location]+1
            tot=tot+temp

print(tot)
