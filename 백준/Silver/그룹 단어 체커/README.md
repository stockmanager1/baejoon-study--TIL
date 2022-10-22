# 1트
'happy'를 ['h', 'a', 'pp', 'y']로 이런 리스트를 만들려고 했는데 결국 실패함.

```
for i in range(len(k)):
  if i == len(k) - 1:
    break
  else:
    pass
  if k[i] != k[i+1]:
    new_words.append(k[i])
  else:
    a = i
```
이리저리 해보려고 했는데 결국 실패했다.

# 답안
```
n=int(input())
cnt=0
for _ in range(n):
    word=input()
    for i in range(len(word)-1):
        if word[i]!=word[i+1]:
            if word[i] in word[i+1:]:
                n-=1
                break
print(n)
``` 
이 문제를 풀고 알게된 점이 있다.

1. str문도 리스트처럼 리스트 길이(len), 슬라이싱([])이 모두다 가능하다는 거다.

위 답안도 이런식으로 풀었는데, 앞으로 이런 방법으로 접근해보면 좋을 것 같다.
