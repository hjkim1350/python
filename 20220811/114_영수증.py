# https://www.acmicpc.net/problem/25304
# 구매한 각 물건의 가격과 개수, 총 금액을 계산하여 영수증의 총 금액과 비교
# Input 첫번째줄: 총 금액 X
# Input 두번째줄: 구매한 물건 종류 수 N
# Input 세번째줄~마지막: 물건의 가격a과 개수b가 공백을 사이에 두고 주어짐

X = int(input())
N = int(input())

total = 0

for _ in range(N):
    a, b = map(int, input().split())
    total += a * b

# if 삼항연산자 연습
print("Yes") if X == total else print("No")