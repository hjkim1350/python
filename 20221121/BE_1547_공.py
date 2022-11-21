# https://www.acmicpc.net/problem/1547
# 공은 1번 위치에 있으며 컵만 서로 맞교환함
# 공이 있는 컵 번호 출력

ball = 1

for i in range(int(input())):
    X, Y = map(int, input().split())
    if ball == X:
        ball = Y
    elif ball == Y:
        ball = X

print(ball)