# 1트

```
n = int(input()) * 2
a = []
for i in range(n):
  a.append(int(input()))

new_a = []

for i in a:
  if i % 2 == 0:
    pass
  else:
    new_a.append()
```
2차원 배열을 억지로 내가 만들려고 해서 틀림

# 2트

```
A = int(input())
B = int(input())
list_A = []
for i in range(1,B+1):
  list_A.append(i)
step_list = []
step_list.append(list_A)
list_B = []
for i in range(B):
  alpha = step_list[i]
  for j in alpha:
    sum = 0
    sum = sum + j
    list_B.append(sum)

```
# 3트
```
n = 2

for i in range(n):
  A = int(input())
  B = int(input())

  list_A = []

  list_B = []

  for i in range(1,list_D[]1):
    list_B.append(i)
  
  list_A.append(list_B)

  for i in range(A):
    list_A.append([])
  
  sum = 0

  for i in range(len(list_A)-1):
    for j in range(B):
      sum = sum + list_A[i][j]
      list_A[i+1].append(sum)
    sum = 0    
  print(list_A[A][B-1])
```

# 4트
```
a = int(input())
b = int(input())


first_step = []

# 0층을 구현하기
for i in range(1,b+1):
  first_step.append(i)
  
#슬라이싱으로 각 층이 되는 조건을 구현할 수 있을까?
#2번째 층을 구하기 위해서는 1번쨰 층을 반드시 알아야 구현이 가능하다.
#그러면 구하는 층의 이전 층을 알아야 한다.
under_step = []

count = len(first_step)

for i in range(count):
  if i == 0:
    for j in range(len(first_step)):
      k = []
      k.append(first_step[0:j+1])
      c = sum(k,[])
      under_step.append(sum(c))
  else:
    for j in range(len(first_step)):
      k = []
      k.append(under_step[0:j+1])
      c = sum(k,[])
      under_step.append(sum(c))
```

# 정답 코드
```
t = int(input())

for _ in range(t):  
    floor = int(input())  # 층
    num = int(input())  # 호
    f0 = [x for x in range(1, num+1)]  # 0층 리스트
    for k in range(floor):  # 층 수 만큼 반복
        for i in range(1, num):  # 1 ~ n-1까지 (인덱스로 사용)
            f0[i] += f0[i-1]  # 층별 각 호실의 사람 수를 변경
    print(f0[-1])  # 가장 마지막 수 출력
```
계속 리스트의 sum함수에 의존해서 문제를 풀려는 경향이 강하다.

그래서 계속 sum을 쓰려고 함
