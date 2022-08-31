# https://www.acmicpc.net/problem/1357
# 두 양의 정수 X, Y 주어졌을 때 모든 자리 수 역순으로 더한 값의 역순 출력

X, Y = input().split()

rev_X = int(X[::-1])
rev_Y = int(Y[::-1])

sum = str(rev_X + rev_Y)
rev_sum = int(sum[::-1])

print(rev_sum)