# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpoFaAS4DFAUq&categoryId=AV5PpoFaAS4DFAUq&categoryType=CODE&problemTitle=1959&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
# 두개의 리스트 주어짐, 짧은 리스트는 한칸씩 옮길 수 있음
# 이 때 마주보는(즉 index가 같을 때) 요소들의 곱 중 가장 큰 값 구하기

# 문제 풀이 전략
# 짧은 인덱스를 기준으로 긴 인덱스를 순차적으로 순회하여 값을 저장

# input 값 파일로 읽어들이기
import sys

sys.stdin = open("D2_1959_두개의숫자열.txt", "r")

# 테스트 케이스 수 T 처리
T = int(input())

for tc in range(1, T + 1):
    # N, M 처리
    N, M = map(int, input().split())

    # A, B 요소를 list로 저장
    A_list = list(map(int, input().split()))
    B_list = list(map(int, input().split()))

    # 결과값 저장

    max_result = 0

    # A, B 리스트 swab하여 항상 A가 길고, N이 크도록 변수값 변경
    if len(B_list) > len(A_list):
        N, M = M, N
        A_list, B_list = B_list, A_list

    # A, B 리스트 개수가 동일한 경우
    if N == M:
        result = 0

        for i in range(N):
            result += A_list[i] * B_list[i]

            if result > max_result:
                max_result = result
        print("#{tc} {max_result}")

    # A 리스트 개수가 동일하지 않은 경우
    else:
        for i in range(N - M + 1):
            result = 0
            for j in range(M):
                result += A_list[j + i] * B_list[j]

            if result > max_result:
                max_result = result
        print(f"#{tc} {max_result}")
