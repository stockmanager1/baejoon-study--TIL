dp = [0] * (100+1)

dp[1] = 1
dp[2] = 1
dp[3] = 1

for i in range(4,101):
  dp[i] = dp[i-2] + dp[i-3]


n = int(input())
for i in range(n):
  num = int(input())
  print(dp[num])