# https://www.acmicpc.net/problem/2511
# Input 첫번째줄: A가 뒤집은 카드의 숫자
# Input 두번째줄: B가 뒤집은 카드의 숫자
# 이긴사람에게 3점, 비기면 각각 1점
# Output 첫번째줄: A의 득점, B의 득점
# Output 두번째줄: 승자

import sys
sys.stdin = open("test.txt")

A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

A_score = 0
B_score = 0
winner = []

for i in range(10):
    if A_list[i] > B_list[i]:
        A_score += 3
        winner.append("A")
    elif A_list[i] < B_list[i]:
        B_score += 3
        winner.append("B")
    else:
        A_score += 1
        B_score += 1
        winner.append("D")

print(A_score, B_score)

if A_score > B_score:
    print("A")
elif A_score < B_score:
    print("B")
else:
    j = 9
    
    while j:
        if winner[j] != "D":
            print(winner[j])
            break
        j -= 1
    
    if j == 0:
        print("D")