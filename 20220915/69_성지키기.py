# https://www.acmicpc.net/problem/1236
# 첫번째줄 성의 세로크기 N과 가로크기 M이 주어짐
# 성의 모든 행과 모든 열에는 1명 이상의 경비원이 존재하여야 함
# 추가해야할 경비원 수 구하기

N, M = map(int, input().split())
cnt = 0

# 행
for _ in range(N):
    row = input()

    if "X" not in row:
        cnt += 1

print(cnt)