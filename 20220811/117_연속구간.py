# https://www.acmicpc.net/problem/2495
# 8자리 양의 정수에 연속되는 숫자가 있는지 확인
# 없으면 1 출력 있으면 연속되는 숫자 중 가장 큰 숫자 출력

import sys
sys.stdin = open("test.txt")

while True:
    try:
        N = input()
        max_list = []
        cnt = 1

        if N == "#":
            break

        for i in range(len(N)-1):
            if N[i] == N[i+1]:
                cnt += 1
                max_list.append(cnt)
            else:
                if cnt > 1:
                    max_list.append(cnt)
                    cnt = 1
        print("1") if len(max_list) == 0 else print(max(max_list))
    
    except:
        break