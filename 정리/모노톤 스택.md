# 모노톤스택 monotone stack

스택들의 원소들을 (중복없는) 오름차순 및 내림차순 상태를 유지하도록 하여 시간복잡도를 획기적으로 줄여주는 알고리즘 테크닉

-- 대표적으로 "현재값보다 작은(or 큰) 가장 근접한 요소"를 찾는 알고리즘의 문제로 사용됨(O(n)만에 풀 수 있는 강력한 풀이법)



### BOJ 2493 탑

```python
n = int(input())
arr = [1000000000] + list(map(int, input().split()))

stack = []
stack.append(0) # 스택에는 인덱스를 저장, 처음에는 arr[0]인 1000000000을 넣는다고 보면 됨

for i in range(1, n + 1):
    while arr[i] > arr[stack[-1]]: # 지금 넣으려고 하는 수보다 stack의 top에 있는 수가 더 작으면 다 꺼내고 넣어
        stack.pop()

    print(stack[-1], end=' ')
    stack.append(i)
```



### why O(n)?

```
for문 한번에 while문이 중첩되어있어서 육안으로 보기에는 O(n제곱)처럼 보이지만 코드를 자세히 보면

stack.pop의 실행수 <= stack.append의 실행수 == n
즉 append는 n번 실행되며 pop은 append 수보다 클 수 없다. 
for문 안에서 진행되는 전체 pop의 실행수가 while의 시간복잡도와 같으므로 for문 전체의 시간복잡도는 amortized O(n)이된다.
```



### BOJ 17298 오큰수

```python
n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
# 각 원소에 대해 오른쪽에 있으면서 큰 수가 없는경우 오큰수는 default가 -1이므로 -1로 채워놓고 덮어씌우기
answer = [-1] * n 

stack = []
stack.append(0)

for i in range(1, n):
    while stack and arr[stack[-1]] < arr[i]: # 지금 넣으려는 수보다 stack의 top에 있는 수가 더 작으면 다 꺼내
        answer[stack.pop()] = arr[i]	# 꺼내면서 answer의 pop한 인덱스를 덮어씌우기
    stack.append(i)

print(*answer)
```

