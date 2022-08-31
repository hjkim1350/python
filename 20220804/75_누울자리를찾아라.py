# https://www.acmicpc.net/problem/1652
# N x N 방 크기에 연속해서 2칸 이상의 빈자리가 날 경우 누울 수 있음
# 가로로 누울 수 있는 자리, 세로로 누울 수 있는 자리 출력

N = int(input())

room = [list(input()) for _ in range(N)]
row = 0
column = 0

# 가로 누울 자리 찾기
for i in range(N):
    cnt1 = 0
    for j in range(N):
        if room[i][j] == '.':
            cnt1 += 1
        else:
            cnt1 = 0
        
        if cnt1 == 2:
            row += 1

# 세로 누울 자리 찾기
for i in range(N):
    cnt2 = 0
    for j in range(N):
        if room[j][i] == '.':
            cnt2 += 1
        else:
            cnt2 = 0
        
        if cnt2 == 2:
            column += 1

print(row, column)