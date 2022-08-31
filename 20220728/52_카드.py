# https://www.acmicpc.net/problem/11652
# 준규가 가지고 있는 카드가 주어졌을 때 가장 많이 가지고 있는 정수 구하기
# Input 첫째줄: 준규가 가지고 있는 숫자 카드 개수
# Input 둘째줄~끝: N개줄에 숫자 카드에 적혀있는 정수

N = int(input())

cards = {}

for i in range (0, N):
    card = int(input())

    if card not in cards:
        cards.setdefault(card, 1)
    else:
        cards[card] = cards.get(card) + 1

cards_sort = dict(sorted(cards.items()))

print(max(cards_sort, key=cards_sort.get))