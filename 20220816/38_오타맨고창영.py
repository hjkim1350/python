# https://www.acmicpc.net/problem/2711
# 주어진 문자열 내 오타 지우고 출력하기
# 첫 숫자는 창영이가 오타낸 위치, 두번째 문자열은 창영이가 입력한 문자열

import sys
sys.stdin = open("test.txt")

N = int(input())

for i in range(N):
    idx, stc = input().split()
    idx = int(idx)-1
    
    if idx == 0:
        print(stc[1:])
    else:
        print(stc[0:idx] + stc[idx+1:])