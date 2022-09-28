# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PnnU6AOsDFAUq&categoryId=AV5PnnU6AOsDFAUq&categoryType=CODE&problemTitle=1948&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
# 첫번째줄: 테스트 케이스 수
# 두번째줄~마지막줄: 월 일 월 일
# 결과값: 첫번쨰 월 일로부터 두번째 월 일까지 며칠째인지 출력
# 풀이전략: (첫번째 월의 마지막날-첫번째 주어진 일+1)+주어진 날 사이의 월 처리+두번째 일

# input 값 파일로 읽어들이기
import sys
sys.stdin = open("D2_1948_날짜계산기.txt", "r")

# 테스트 케이스 수 T 처리
T = int(input())

# 월 일 dic 정의
cal = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

# 테스트 케이스 수 T 만큼 반복하여 수행
for test_case in range(1, T+1):
    # 날짜수 계산
    cnt = 0

    # 월, 일 처리
    m1, d1, m2, d2 = map(int, input().split())

    # (첫번째 월의 마지막날-첫번째 주어진 일+1)
    cnt = cal[m1] - d1 + 1

    # 주어진 날 사이의 월 처리
    if m1 != m2:
        for i in range(m1+1, m2):
            cnt += cal[i]
    # 마지막 달 처리
        cnt += d2

    print(f"#{test_case}",cnt)