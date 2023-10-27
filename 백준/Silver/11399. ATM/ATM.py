n = int(input())

list_A =list(map(int,input().split()))

list_A.sort()

dp = [0] * (n+1)
dp[0] = list_A[0]
for i in range(1,n):
  dp[i] = dp[i-1] + list_A[i]

print(sum(dp))