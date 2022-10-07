# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PsIl6AXIDFAUq&categoryId=AV5PsIl6AXIDFAUq&categoryType=CODE&problemTitle=1970&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
# 손님 거스름돈 최소 개수로 거슬러주기 위해 몇 개씩 필요한지 출력

# input 값 파일로 읽어들이기
import sys

sys.stdin = open("D2_1970_쉬운거스름돈.txt", "r")

# 테스트 케이스 수 T 처리
T = int(input())

for tc in range(1, T + 1):
    # N 처리 - 손님에게 거슬러줄 총 액수
    N = int(input())

    # 거스름돈 dic 정의
    N_dic = {
        50000: 0,
        10000: 0,
        5000: 0,
        1000: 0,
        500: 0,
        1000: 0,
        500: 0,
        100: 0,
        50: 0,
        10: 0,
    }

    for i in N_dic.keys():
        if N >= i:
            N_dic[i] = N // i
            N %= i

    print(f"#{tc} ")
    for i in N_dic.values():
        print(i, end=" ")

    print()
