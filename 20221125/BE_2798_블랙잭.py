# https://www.acmicpc.net/problem/2798
# N장의 카드 숫자 합이 M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 출력

N, M = map(int, input().split())
cards = list(map(int, input().split()))
result = []

for i in range(N):
    for j in range(i+1, N):
        for h in range(j+1, N):
            cards_sum = cards[i] + cards[j] + cards[h]
            if  cards_sum > M:
                continue
            else:
                result.append(cards_sum)

print(max(result))