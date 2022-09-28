# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PobmqAPoDFAUq&categoryId=AV5PobmqAPoDFAUq&categoryType=CODE&problemTitle=1954&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
# 주어진 숫자의 달팽이 숫자 출력하기
# 예를 들어 3이 주어지면 하기와 같이 출력
# 1 2 3
# 8 9 4
# 7 6 5
# 행 순회 > 열순회 > 행 역순회 > 열 역순회 > 행 순회... 반복

# pprint 모듈 가져오기
from functools import cmp_to_key
from pprint import pprint

# input 값 파일로 읽어들이기
import sys
sys.stdin = open("D2_1954_달팽이숫자.txt", "r")

# 테스트 케이스 수 T 처리
T = int(input())

# 테스트 케이스 수 T 만큼 반복하여 수행
for tc in range(1, T+1):
    # 달팽이 수 받기
    N = int(input())

    # 달팽이 담을 이차원 배열 선언
    N_list = []
    for _ in range(N):
        N_list.append([0] * N)
    
    # 달팽이에 들어갈 숫자 카운트
    cnt = 1

    # N바퀴 돌리기
    for i in range(0, N):
        # 1) 행 순회
        for j in range(i, N-i):
            N_list[i][j] = cnt
            cnt += 1
        
        # 2) 열 순회
        for j in range(i+1, N-i):
            N_list[j][N-1-i] = cnt
            cnt += 1
        
        # 3) 행 역순회
        for j in range(N-(1+2*i)):
            N_list[N-1-i][N-2-j] = cnt
            cnt += 1

        # 4) 열 역순회
        for j in range(i+1, N-(i+1)):
            N_list[N-(i+1)-j][i] = cnt
            cnt += 1


    # # 첫 행 순회
    # for i in range(0, N):
    #     N_list[0][i] = cnt
    #     cnt += 1
    
    # # 첫 끝 열 순회
    # for i in range(1, N):
    #     N_list[i][N-1] = cnt
    #     cnt += 1
    
    # # 마지막 행 역순회
    # for i in range(N-1):
    #     N_list[N-1][N-2-i] = cnt
    #     cnt += 1
    
    # # 마지막 열 역순회
    # for i in range(1, N-1):
    #     N_list[N-1-i][0] = cnt
    #     cnt += 1
    
    # # 두번째 행 순회
    # for i in range(1, N-1):
    #     N_list[1][i] = cnt
    #     cnt += 1

    # # 두번째 끝 열 순회
    # for i in range(2, N-1):
    #     N_list[i][N-2] = cnt
    #     cnt += 1
    
    # # 두번째 끝 행 역순회
    # for i in range(N-3):
    #     N_list[N-2][N-3-i] = cnt
    #     cnt += 1

    # 결과 출력
    print(f"#{tc}")
    pprint(N_list)