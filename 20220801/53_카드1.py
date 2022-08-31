# https://www.acmicpc.net/problem/2161
# 제일 위 카드는 버리고 그 다음 제일 위 카드는 맨 밑으로 보내기
# 이에 따라 카드 N장이 있을 때 버린 카드를 순서대로 출력 후 마지막에 남게되는 카드 출력

N = int(input())
N_list = []
N_pop_list = []

# N장의 카드 쌓기
for i in range(1, N+1):
    N_list.append(N+1-i)

# 카드 버리고 맨 밑으로 보내기
while len(N_list) != 1:
    # 카드 버리기
    N_pop_list.append(N_list.pop())
    
    # 맨 밑으로 보내기
    N_list.insert(0, N_list.pop())

# 마지막 남은 숫자 리스트에 포함
N_pop_list.append(N_list.pop())

for j in range(len(N_pop_list)):
    print(N_pop_list[j], end=' ')