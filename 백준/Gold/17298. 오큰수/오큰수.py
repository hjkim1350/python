N = int(input())
N_list = list(map(int, input().split()))
stack = []
result = [-1] * N

for i in range(N):
    while stack and N_list[stack[-1]] < N_list[i]:
        result[stack.pop()] = N_list[i]
    stack.append(i)

print(*result)