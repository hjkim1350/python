# https://www.acmicpc.net/problem/10816
# 숫자 카드 몇개 쥐고 있는지 수를 구하기
# Input 첫째줄: 상근이가 쥐고 있는 카드 총 숫자 (둘째줄 카드 수)
# Input 둘째줄: 상근이가 쥐고 있는 카드의 정수값 나열
# Input 셋째줄: 구해야할 정수 카드의 숫자 (넷째줄 카드 수)
# Input 넷째줄: 상근이가 몇개 가지고 있는지 기준이 되는 카드의 정수값

# Input 첫째줄, 둘째줄 처리
N = int(input())
N_card = list(map(int, input().split()))
N_dic = {}

# 상근이가 쥐고 있는 카드를 딕셔너리에 담기
for i in range(N):
    if N_card[i] not in N_dic:
        N_dic.setdefault(N_card[i], 1)
    else:
        N_dic[N_card[i]] = N_dic.get(N_card[i]) + 1

# Input 셋째줄, 넷째줄 처리
M = int(input())
M_card = list(map(int, input().split()))

for j in range(M):
    if N_dic.get(M_card[j]) == None:
        print("0", end=' ')
    else:
        print(N_dic.get(M_card[j]), end=' ')