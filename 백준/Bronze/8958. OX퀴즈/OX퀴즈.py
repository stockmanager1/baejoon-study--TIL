#n값 구하기
n = int(input())
E = []
#ox값 받기
for i in range(n):
    a= input().split('X')
    a = ' '.join(a).split()

#각 a값을 리스트로 받아야 한다.
    for i in a:
      C = list(i)

      i = 0
      sum = 0
      for i in range(0,len(C)+1):
        sum=sum+i

      E.append(sum)
    sum = 0
    for i in E:
      sum = sum + i
    print(sum)
    E.clear()
