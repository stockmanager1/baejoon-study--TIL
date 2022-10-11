# 1트 eval 사용


```
n = input().split('-')
new_list = []
for i in n:
  k = list(i)
  for j in range(len(k)):
    if k[0] == '0':
      del (k[0])
    else:
      pass
  a = ''.join(k)
  new_list.append(a)
new_new_list = []
if len(new_list) == 1:
  print(eval(new_list[0]))
else:
  for i in new_list:
    new_new_list.append(eval(i))
  new_new_list = list(map(str,new_new_list))
  new_new_new_list = '-'.join(new_new_list)
  print(eval(new_new_new_list))

```

eval을 쓰면 런타임 에러가 난다는 구글링 결과를 보고 다른 방법을 생각해 보기로 했다.

## 배운점

1. 0009 + 0009를 컴퓨터는 연산할 수 없다.
2. 다시 한번 join함수에 대해 생각하게 되었다.
    
    (append는 리스트, join은 문자열)
    
# 2트 : eval을 사용하되 00009같은 숫자는 무조건 0이 나와야 한다. 

```
print(eval('009-009'))
```
-----> SyntaxError: invalid token
0009같은 숫자는 계산 자체가 불가능함.

# 3트
```
n = input().split('-')

new_list = []

for i in n:
  k = list(i)
  for j in range(len(k)):
    if k[0] == '0':
      del (k[0])
    else:
      pass
  a = ''.join(k)
  new_list.append(a)

new_list = list(map(str,new_list))

if len(new_list) == 1:
  print(eval(new_list))
else:
  final = eval('-'.join(new_list))
  print(final)
```

eval을 사용하면 안될듯 애초에 eval을 사용하지마라고 0009를 배치한듯.

# 결국 구글링

```
a = input().split('-')
num = []
for i in a:
    cnt = 0
    s = i.split('+')
    for j in s:
        cnt += int(j)
    num.append(cnt)
n = num[0]
for i in range(1, len(num)):
    n -= num[i]
print(n)
```

## 내가 틀린이유
1. split에 대해 좀 더 깊은 이해가 필요하다. 단순히 input().split()처럼 문자를 받을때만 사용하는 것이 아니다.
2.계속 한가지 방법론에만 집착한다. 여기서는 eval 함수를 사용해서 푸는 것에 너무 집착했다.
3. 리스트 내부 요소끼리 빼기 연산을 할 줄 몰랐다.
4. 더하기도 마찬가지다. 너무 sum함수에만 의존해서 문제를 푸는 경향이 너무 심했다. 물론 편하고 빠르겠지만 이런 방법도 알아야 한다.
5.0009연산을 어떻게 처리해야 하는지 모르겠다.

# 4트: 예외처리와 strip함수를 사용해서 풀어보자.

```
n = input().split('-')

new_list = []

cnt = 0

try:
  for i in n:
    k = eval(i)
    new_list.append(k)
  if len(new_list) == 1:
    print(new_list[0])
  else:
    for i in new_list:
      cnt = new_list[0]
      cnt = cnt - i
    print(cnt)
except SyntaxError:
  for i in n:
    k = i.strip('0')
    new_list.append(k)
  new_list = list(map(int,new_list))
  for i in new_list:
    cnt = new_list[0]
    cnt = cnt - i
  print(cnt)
```

일단 틀렸다고 나온다.

03+03을 처리할 수가 없음.

## 내가 결국 못푼이유
1. 예외처리를 하면 0009-0009를 해결 할 수 있을 줄 알았다.
2. 실제로 해결하기는 했지만 03+03은 걸러지지 못함.
3.약간 오기로 미워도 다시한번이라 말하며 푼거라....
4. 이중 반복믈 사용하는거에 대한 거부감이 너무 든다. 그래서 계속 틀리는듯?

[strip함수](https://github.com/stockmanager1/python-insight-collection/blob/main/strip%ED%95%A8%EC%88%98/README.md)

이거 반복문으로 strip을 돌리면 풀리기는 할거 같은데 너무 지저분해진다.ㅠㅠㅠ
