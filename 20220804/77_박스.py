# https://www.acmicpc.net/problem/9455
# 박스가 바닥에 쌓일때까지 이동한 거리

T = int(input())

for _ in range(T):
    m, n = map(int, input().split())

    box = [list(map(int, input().split())) for _ in range(m)]
    tmp = 0

    move_len = 0

    for i in range(0, m-1):
        for j in range(0, n-1):
            if box[j][i] == 1:
                if box[j+1][i] == 0:
                    box[j][i] = 0
                    box[j+1][i] = 1
                    move_len += 1
                    print(box)
                    print(move_len)
                else:
                    continue
        