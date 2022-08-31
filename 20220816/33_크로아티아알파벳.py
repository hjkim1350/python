# https://www.acmicpc.net/problem/2941
# 크로아티아 알파벳 글자수 세기
# c=, c- 과 같이 제시된 글자는 2글자 등이 아닌 1글자로 카운팅

import sys
sys.stdin = open("test.txt")

N = input()
N_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in N_alpha:
    N = N.replace(i, '*')

print(len(N))