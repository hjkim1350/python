# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Pq-OKAVYDFAUq&categoryId=AV5Pq-OKAVYDFAUq&categoryType=CODE&problemTitle=1961&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
# 배열 시계방향으로 90도, 180도, 270도 회전한 모양 출력


# input 값 파일로 읽어들이기
import sys

sys.stdin = open("D2_1961_숫자배열회전.txt", "r")

# 테스트 케이스 수 T 처리
T = int(input())

for tc in range(1, T + 1):
    # N 처리
    N = int(input())

    # 2차원 배열 정의
    matrix = []
    matrix = [list(map(int, input().split())) * N for _ in range(N)]

    # 시계방향 90도 회전
    rotated_matrix_90 = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            rotated_matrix_90[i][j] = matrix[N - j - 1][i]

    # 시계방향 180도 회전
    rotated_matrix_180 = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            rotated_matrix_180[i][j] = matrix[N - i - 1][N - j - 1]

    # 시계방향 270도 회전
    rotated_matrix_270 = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            rotated_matrix_270[i][j] = matrix[j][N - i - 1]

    print(f"#{tc}")
    for i in range(N):
        print(*rotated_matrix_90[i], sep="", end=" ")
        print(*rotated_matrix_180[i], sep="", end=" ")
        print(*rotated_matrix_270[i], sep="", end=" ")
        print()
