# https://www.acmicpc.net/problem/9325
# 첫번째줄: 테스트 케이스 수
# 각 테스트 케이스 첫 줄엔 자동차 가격 S
# 테스트 케이스 두번째 줄엔 옵션 개수 N
# 뒤이어 나오는 N개의 줄은 특정 옵션 개수와 옵션의 가격이 주어짐
# 이때 최종적으로 구매하려는 자동차 가격 한줄씩 출력

for i in range(int(input())):
    # 자동차 가격 입력
    S = int(input())
    # 자동차 최종 가격 변수
    total = S

    N = int(input())

    if N != 0:
        for j in range(N):
            p, q = map(int, input().split())
            total += p*q
    
    print(total)