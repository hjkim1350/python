# https://www.acmicpc.net/problem/2857
# FBI 요원 찾기
# 각 줄에 알파벳대문자, 숫자 0~9, 대시로만 이루어져있음
# 몇번째 줄에 요원이 있는지 출력

import sys
sys.stdin = open("test.txt")

cnt = 1
FBI = []

while True:
    # EOF 처리하기 위한 try-except 구문 작성
    try:
        fbi = input()

        if fbi.count("FBI") > 0:
            FBI.append(cnt)
            cnt += 1
        else:
            cnt += 1
            
    except:
        break

if len(FBI) == 0:
    print("HE GOT AWAY!")
else:
    print(*FBI)