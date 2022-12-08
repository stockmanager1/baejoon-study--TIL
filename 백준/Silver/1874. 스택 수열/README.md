# [Silver III] 스택 수열 - 1874 

[문제 링크](https://www.acmicpc.net/problem/1874) 

### 성능 요약

메모리: 132328 KB, 시간: 2372 ms

### 분류

자료 구조(data_structures), 스택(stack)

### 문제 설명

<p>스택 (stack)은 기본적인 자료구조 중 하나로, 컴퓨터 프로그램을 작성할 때 자주 이용되는 개념이다. 스택은 자료를 넣는 (push) 입구와 자료를 뽑는 (pop) 입구가 같아 제일 나중에 들어간 자료가 제일 먼저 나오는 (LIFO, Last in First out) 특성을 가지고 있다.</p>

<p>1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다. 이때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자. 임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지, 있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다. 이를 계산하는 프로그램을 작성하라.</p>

### 입력 

 <p>첫 줄에 n (1 ≤ n ≤ 100,000)이 주어진다. 둘째 줄부터 n개의 줄에는 수열을 이루는 1이상 n이하의 정수가 하나씩 순서대로 주어진다. 물론 같은 정수가 두 번 나오는 일은 없다.</p>

### 출력 

 <p>입력된 수열을 만들기 위해 필요한 연산을 한 줄에 한 개씩 출력한다. push연산은 +로, pop 연산은 -로 표현하도록 한다. 불가능한 경우 NO를 출력한다.</p>


# 1트

```
import sys



n = int(sys.stdin.readline())
balance_list = []
for i in range(1,n+1):
  balance_list.append(int(sys.stdin.readline()))
result = []

num_list =[]

for i in range(1,n+1):
  num_list.append(i)
  result.append('+')
  while True:
    if len(num_list) == 0:
      break
    else:
      pass
    if max(num_list) == balance_list[0]:
      num_list.remove(num_list[len(num_list)-1]) 
      balance_list.remove(balance_list[0])
      result.append('-')
    else:
      break
if len(num_list) != 0:
  print('No')
else:
  for i in result:
    print(i)
```

#2트

```
import sys 

n = int(sys.stdin.readline())


list = []

for i in range(1,n+1):
  list.append(int(sys.stdin.readline()))

balance = []

list_A = []

list_B = []

def recursion(list_A,list_B,list,balance):
  if len(balance) == n:
    return
  if len(list_A) == 0:
    return
  if list_A[-1] == list[0]:
    balance.append(list[0])
    list.remove(list[0])
    list_A.remove(list_A[-1])
    list_B.append('-')
    return recursion(list_A,list_B,list,balance)
  else:
    return


for i in range(1,n+1):
  list_A.append(i)
  list_B.append('+')
  recursion(list_A,list_B,list,balance)
  
if len(list_A) > 1:
  print('N0')
else:
  for i in list_B:
    print(i)
```

#3트
```
n = 8

list = [4,3,6,8,7,5,2,1]

i = 0

balance = []

list_A = []

list_B = []

def recursion(list_A,list_B,list,balance):
  if len(balance) == n:
    return
  if len(list_A) == 0:
    return
  if list_A[-1] == list[0]:
    balance.append(list[0])
    list.remove(list[0])
    list_A.remove(list_A[-1])
    list_B.append('-')
    return recursion(list_A,list_B,list,balance)
  else:
    return
```

#4트

```
import sys 

n = int(sys.stdin.readline())

list_B = []

for i in range(n):
  list_B.append(int(sys.stdin.readline()))

list_B_cp = list_B.copy()

list_C = []
list_A = []
for i in range(1,n+1):
  list_A.append(i)
  list_C.append('+')
  while True:
    if len(list_A) == 0:
      break
    if list_A[-1] == list_B_cp[0]:
      list_A.remove(list_A[-1])
      list_B_cp.remove(list_B_cp[0])
      list_C.append('-')
    else:
      break
if len(list_B_cp) != 0:
  print('NO')
else:
  for i in list_C:
    print(i)
```
