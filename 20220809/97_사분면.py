# https://www.acmicpc.net/problem/9610
# 2차원 좌표 기준 좌표 (x,y)가 주어짐
# 각 사분면과 축에 점 몇개 있는지 구하기

N = int(input())
Q1 = 0
Q2 = 0
Q3 = 0
Q4 = 0
AXIS = 0

for i in range(N):
    x, y = map(int, input().split())
    
    if x == 0 or y == 0:
        AXIS += 1
    elif x > 0 and y > 0:
        Q1 += 1
    elif x < 0 and y > 0:
        Q2 += 1
    elif x < 0 and y < 0:
        Q3 += 1
    else:
        Q4 += 1

print("Q1:", Q1)
print("Q2:", Q2)
print("Q3:", Q3)
print("Q4:", Q4)
print("AXIS:", AXIS)