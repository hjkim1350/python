# https://www.acmicpc.net/problem/15953
# 1회차 때 순위 예상, 2회차 때 순위 예상했을 때 상금의 총 금액구하기

def a_festival (a_nums):
    if a_nums == 1:
        return 5000000
    elif 1 < a_nums <= 3:
        return 3000000
    elif 4 <= a_nums <= 6:
        return 2000000
    elif 7 <= a_nums <= 10:
        return 500000
    elif 11 <= a_nums <= 15:
        return 300000
    elif 16 <= a_nums <= 21:
        return 100000
    else:
        return 0

def b_festival (b_nums):
    if b_nums == 1:
        return 5120000
    elif 2 <= b_nums <= 3:
        return 2560000
    elif 4 <= b_nums <= 7:
        return 1280000
    elif 8 <= b_nums <= 15:
        return 640000
    elif 16 <= b_nums <= 31:
        return 320000
    else:
        return 0

for i in range(int(input())):
    a, b = map(int, input().split())

    print(a_festival(a)+b_festival(b))