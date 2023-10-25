n, k = map(int, input().split())
coin = []

for i in range(n):
    num = int(input())
    coin.append(num)

coin.sort()

cnt = 0
while True:
    if k == 0:
        break
    else:
        if k >= coin[-1]:
            k = k - coin[-1]
            cnt = cnt + 1
        else:
            coin.pop()

print(cnt)