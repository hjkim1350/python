# https://www.acmicpc.net/problem/2750
# N개의 수 오름차순 정렬
# Input 첫째줄은 수의 개수 N
# Input 둘째줄~마지막: 숫자 (숫자는 중복되지 않음)

N_list = []

for i in range(int(input())):
    N_list.append(int(input()))
    N_list.sort()

for j in N_list:
    print(j)