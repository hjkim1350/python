# https://www.acmicpc.net/problem/1065
# 양의 정수 N 각 자리가 등차수열을 이룬다면 그 수는 등차수열
# N이 주어졌을 때 1보다 크거나 같고, N보다 작거나 같은 한수의 개수 출력

N = int(input())

hansu = 0

for i in range(1, N+1):
    N_list = list(map(int, str(i)))

    if i < 100:
        hansu += 1
    
    elif N_list[0]-N_list[1] == N_list[1]-N_list[2]:
        hansu += 1

print(hansu)