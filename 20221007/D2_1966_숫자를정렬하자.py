# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PrmyKAWEDFAUq&categoryId=AV5PrmyKAWEDFAUq&categoryType=CODE&problemTitle=1966&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
# 배열 입력 받아 배열 내 요소들을 순차적으로 정렬

# input 값 파일로 읽어들이기
import sys

sys.stdin = open("D2_1966_숫자를정렬하자.txt", "r")

# 테스트 케이스 수 T 처리
T = int(input())

for tc in range(1, T + 1):
    # N 처리
    N = int(input())

    # 배열 처리
    N_list = list(map(int, input().split()))
    N_list.sort()
    print(f"#{tc}", *N_list)
