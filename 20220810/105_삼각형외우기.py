# https://www.acmicpc.net/problem/10101
# 삼각형 3개 각을 엔터 구분으로 입력받음
# 세 각의 크기가 모두 60이면, Equilateral
# 세 각의 합이 180이고, 두 각이 같은 경우에는 Isosceles
# 세 각의 합이 180이고, 같은 각이 없는 경우에는 Scalene
# 세 각의 합이 180이 아닌 경우에는 Error


t1 = int(input())
t2 = int(input())
t3 = int(input())

if t1 + t2 + t3 == 180:
    if (t1 == t2 == t3 == 60):
        print("Equilateral")
    elif (t1 == t2 or t2 == t3 or t1 == t3):
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")