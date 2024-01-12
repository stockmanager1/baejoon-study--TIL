list_A = input().split('-')

# 첫 번째 항 계산
first_sum = sum(map(int, list_A[0].split('+')))

# 첫 번째 항 이후의 모든 항 계산
rest_sum = sum(sum(map(int, part.split('+'))) for part in list_A[1:])

# 결과 출력
print(first_sum - rest_sum)
