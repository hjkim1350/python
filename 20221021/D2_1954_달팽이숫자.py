# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PobmqAPoDFAUq&categoryId=AV5PobmqAPoDFAUq&categoryType=CODE&problemTitle=1954&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
# 배열 시계방향으로 90도, 180도, 270도 회전한 모양 출력


# input 값 파일로 읽어들이기
import sys

sys.stdin = open("D2_1954_달팽이숫자.txt")


T = int(input())

# 방향 전환 배열
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for test_case in range(1, T + 1):
    
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    i, j, cnt, dr = 0, 0, 1, 0

    arr[i][j] = cnt
    cnt += 1

    while cnt <= N*N:
        # 방향 초기화
        ni, nj = i + di[dr], j + dj[dr]

        # ni, nj는 달팽이 숫자 범위 안이어야 하고 arr에는 숫자 기록없어야 함
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
            i, j = ni, nj
            arr[i][j] = cnt
            cnt += 1
        else:
            dr = (dr+1) % 4

    print(f"#{test_case}")
    for lst in arr:
        print(*lst)