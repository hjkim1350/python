# https://www.acmicpc.net/problem/4396
# n x n 지뢰찾기에 m개의 지뢰가 서로 다른 격자 위에 숨어져있음
# 플레이어는 지점을 건드리다 지뢰 지점을 건드리면 게임에 진다
# 지뢰 없는 지점을 건드리면 상하좌우 또는 대각선에 인접한 8개 칸에
# 지뢰가 몇개 있는지 알려주는 0과 8 사이의 숫자가 나타남

n = int(input())
mines = [list(input()) for _ in range(n)]
opens = [list(input()) for _ in range(n)]

bombs = []

for i in range(1, n-1):
    for j in range(1, n-1):
        bomb = 0
        if opens[i][j] == "x":
            for p in range(i-1, i+2):
                for q in range(j-1, j+2):
                    if mines[p][q] == "*":
                        bomb += 1
            bombs.append(bomb)

print(bombs)