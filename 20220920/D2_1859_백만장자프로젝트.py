# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5LrsUaDxcDFAXc&categoryId=AV5LrsUaDxcDFAXc&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=1
# 첫번째 줄 테스트 케이스 수 T 주어짐
# 다음번째 줄 자연수 N
# 그 다음번째 줄 매매가를 나타내는 N개의 자연수
# 매매는 하루에 1개씩만 가능
# 매매가가 역순이면 아무것도 사지 않는게 최대 이익
# 매매가가 순서대로라면 첫째날, 둘째날 등 앞에 사고 마지막날에 파는게 이득

# input 값 파일로 읽어들이기
import sys
sys.stdin = open("D2_1859_백만장자프로젝트.txt", "r")

# 테스트 케이스 수 T 처리
T = int(input())

# 테스트 케이스 수 T 만큼 반복하여 수행
for test_case in range(1, T+1):
    # 매매가 수를 나타내는 N 처리
    N = int(input())

    # 매매가를 list로 저장
    trade = list(map(int, input().split()))

    print(f"#{test_case}", max(trade))