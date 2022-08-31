# https://www.acmicpc.net/problem/5576
# 각 팀 중 가장 높은 3개의 점수의 합산 비교

W_score = []
K_score = []

for i in range(10):
    W_score.append(int(input()))

for j in range(10):
    K_score.append(int(input()))

W_score.sort(reverse=True)
K_score.sort(reverse=True)

print(sum(W_score[:3]), sum(K_score[:3]))