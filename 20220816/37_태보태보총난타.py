# https://www.acmicpc.net/problem/17249
# (^0^) 얼굴 기점으로, 왼쪽 난타(@)와 오른쪽 난타(@) 숫자 세기

N = input()
left = 0
right = 0

for i in N:
    if i != '(':
        if i == '@':
            left += 1
    else:
        break

start = int(N.find(')')) + 1

for j in range(start, len(N)):
    if N[j] == '@':
        right += 1

print(left, right)