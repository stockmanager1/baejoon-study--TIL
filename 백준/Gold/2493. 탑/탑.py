N = int(input())
build = list(map(int, input().split()))
result = [0] * N  # 초기화된 결과 리스트

stack = []  # 인덱스를 저장하는 스택
for i in range(N):
    while stack and build[stack[-1]] < build[i]:  # 스택이 비어있지 않고 현재 탑보다 높은 탑이 있다면
        stack.pop()  # 높이가 낮은 탑은 제거
    if stack:  # 스택이 비어있지 않으면
        result[i] = stack[-1] + 1  # 현재 탑의 수신 탑은 스택의 가장 위에 있는 탑
    stack.append(i)  # 현재 탑의 인덱스를 스택에 추가

result = ' '.join(map(str, result))
print(result)
