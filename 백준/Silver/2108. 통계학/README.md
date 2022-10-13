# [Silver III] 통계학 - 2108 

[문제 링크](https://www.acmicpc.net/problem/2108) 

### 성능 요약

메모리: 52296 KB, 시간: 544 ms

### 분류

구현(implementation), 수학(math), 정렬(sorting)

### 문제 설명

<p>수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.</p>

<ol>
	<li>산술평균 : N개의 수들의 합을 N으로 나눈 값</li>
	<li>중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값</li>
	<li>최빈값 : N개의 수들 중 가장 많이 나타나는 값</li>
	<li>범위 : N개의 수들 중 최댓값과 최솟값의 차이</li>
</ol>

<p>N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 단, N은 홀수이다. 그 다음 N개의 줄에는 정수들이 주어진다. 입력되는 정수의 절댓값은 4,000을 넘지 않는다.</p>

### 출력 

 <p>첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.</p>

<p>둘째 줄에는 중앙값을 출력한다.</p>

<p>셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.</p>

<p>넷째 줄에는 범위를 출력한다.</p>

# 1트
```
n = int(input())

first_list = []
for i in range(n):
  first_list.append(int(input()))
first_list.sort()

print(round(sum(first_list)/len(first_list)))

import math

mid = math.floor(len(first_list)/2)
print(first_list[mid])

from collections import Counter

k = Counter(first_list)

value_copy = list(map(int,k.values()))

value_copy = set(value_copy)

list_B = []

if len(first_list) == 1:
  print(first_list[0])
elif len(value_copy) < len(k.values()):
  for i in k.keys():
    if k[i] == max(k.values()):
      list_B.append(i)
  del list_B[0]
  print(list_B[0])
elif len(value_copy) == len(k.values()):
    for i in k.keys():
      if k[i] == max(k.values()):
        del k[i]
        break
    for i in k.keys():
      if k[i] == max(k.values()):
        print(i)

if max(first_list) >0 and  min(first_list) >0:
  print(max(first_list) - min(first_list))
elif max(first_list) <0 and min(first_list) >0:
  print(-(max(first_list)) - min(first_list))
elif max(first_list) >0 and  min(first_list) <0:
  print((max(first_list)) + min(first_list))
elif max(first_list) <0 and  min(first_list) <0:
  print(-(max(first_list)) + min(first_list))
elif max(first_list) == 0:
  print((max(first_list)) - min(first_list))
elif min(first_list) == 0:
  print((max(first_list)) + min(first_list))
```
너무 복잡하게 풀었다.

# 2트
```
n = int(input())

first_list = []
for i in range(n):
  first_list.append(int(input()))
first_list.sort()

print(round(sum(first_list)/len(first_list)))

import math

mid = math.floor(len(first_list)/2)
print(first_list[mid])

first_list = sorted(first_list)

first_list_copy = first_list.copy()

from collections import Counter

k = Counter(first_list)
if len(first_list) == 1:
  print(first_list[0])
elif max(first_list) == 1:
  print(first_list[1])
elif len(first_list)>=2:  
  for i in k.keys():
    if k[i] == max(k.values()):
      first_list_copy.remove(i)
      break
  print(max(first_list_copy))

final = max(first_list) - min(first_list)


print(final)
```
최빈값에 대한 오류가 발생

# 3트(딕션을 정렬하고 반복문으로 리스트를 만들기)
```
n = int(input())

first_list = []
for i in range(n):
  first_list.append(int(input()))
first_list.sort()

print(round(sum(first_list)/len(first_list)))

import math

mid = math.floor(len(first_list)/2)
print(first_list[mid])

first_list = sorted(first_list)


from collections import Counter


k = Counter(first_list)


if len(first_list) == 1:
  print(first_list[0])

elif max(k.values()) == 1:
  print(first_list[1])

elif max(k.values()) >= 2:
  k1 = sorted(k.items(),reverse = True)
  k1 = dict(k1)
  new_list = []
  for key,value in k1.items():
    for i in range(value):
      new_list.append(key)
  print(new_list[1])

final = max(first_list) - min(first_list)
print(final)
```
이거 collections의 most_commom 함수를 몰라 좀 해맸다. 다음에는 이걸로 풀어야지

# 4트(most_common)
```
import sys 
from collections import Counter

#main
t = int(sys.stdin.readline())

numbers = []
for _ in range(t):
    numbers.append(int(sys.stdin.readline()))
    
def mean(nums):
    return round(sum(nums)/len(nums))

def median(nums):
    nums.sort()
    mid = nums[len(nums)//2] # nums의 개수는 홀수
    
    return mid

def mode(nums):
    mode_dict = Counter(nums)
    modes = mode_dict.most_common()    
    
    if len(nums) > 1 : 
        if modes[0][1] == modes[1][1]:
            mod = modes[1][0]
        else : 
            mod = modes[0][0]
    else : 
        mod = modes[0][0]

    return mod
        
def scope(nums):
    return max(nums) - min(nums)

print(mean(numbers))
print(median(numbers))
print(mode(numbers))
print(scope(numbers))
```

# 새롭게 알게된 사실
1. 튜플을 k[0][1]이런 형식으로 출력이 가능하다.
2. most_common으로 최빈값들의 갯수를 알 수 있다. 이게 튜플로 리턴됨. count와 함께 앞으로 유용하게 쓰일듯하다.
