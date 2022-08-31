# https://www.acmicpc.net/problem/2789
# CAMBRIDGE 에 포함된 모든 알파벳은 지우기


N = input()

for i in N:
    if i in 'CAMBRIDGE':
        N = N.replace(i, '')

print(N)