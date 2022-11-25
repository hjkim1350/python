# https://www.acmicpc.net/problem/1453
# 첫번째 줄에는 손님 수 N
# 두번째 줄에는 손님 들어오는 순서대로 손님 앉고 싶어하는 자리가 주어짐

N = int(input())
customer = list(map(int, input().split()))
customer_dict = {}
reject_customer = 0

for i in range(N):
    if customer[i] not in customer_dict:
        customer_dict[customer[i]] = 1
    else:
        reject_customer += 1

print(reject_customer)