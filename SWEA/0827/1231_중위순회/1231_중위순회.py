import sys
sys.stdin = open('input.txt')

# def inorder(cur=1):     # 왼, 부, 오
#     if l_child.get(cur):
#         inorder(l_child[cur])
#
#     print(char[cur], end='')
#
#     if r_child.get((cur)):
#         inorder(r_child[cur])
#
# for k in range(1, 11):
#     N = int(input())
#     temp = [input().split() for i in range(N)] # 일단 입력 받아
#     char = [0 for i in range(N + 1)] # 노드 번호마다 문자 매치
#     l_child = {}
#     r_child = {}
#     for i in range(len(temp)): # 왼쪽 오른쪽 서브트리 따로관리
#         char[int(temp[i][0])] = temp[i][1]
#         if len(temp[i][2:]) == 1:
#             l_child[int(temp[i][0])] = int(temp[i][2])
#         if len(temp[i][2:]) == 2:
#             l_child[int(temp[i][0])] = int(temp[i][2])
#             r_child[int(temp[i][0])] = int(temp[i][3])
#     print('#{}'.format(k), end=' ')
#     inorder()
#     print()

##############################

# 같은로직, 완전이진트리이므로 이렇게도 가능
def inorder(cur=1):  # 왼, 부, 오
    if cur > N:
        return

    inorder(2 * cur)
    print(char[cur], end='')
    inorder(2 * cur + 1)

for k in range(1, 11):
    N = int(input())
    temp = [input().split() for i in range(N)]  # 일단 입력 받아
    char = [0 for i in range(N + 1)]  # 노드 번호마다 문자 매치
    for i in range(len(temp)):
        char[int(temp[i][0])] = temp[i][1]
    print('#{}'.format(k), end=' ')
    inorder()
    print()
