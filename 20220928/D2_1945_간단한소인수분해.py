# input 값 파일로 읽어들이기
import sys

sys.stdin = open("D2_1945_간단한소인수분해.txt", "r")

# 테스트 케이스 수 T 처리
T = int(input())
result = []

for i in range(1, T + 1):
    N = int(input())
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0

    while N % 2 == 0:
        N //= 2
        a += 1
    while N % 3 == 0:
        N //= 3
        b += 1
    while N % 5 == 0:
        N //= 5
        c += 1
    while N % 7 == 0:
        N //= 7
        d += 1
    while N % 11 == 0:
        N //= 11
        e += 1

    print(f"#{i} {a} {b} {c} {d} {e}")
