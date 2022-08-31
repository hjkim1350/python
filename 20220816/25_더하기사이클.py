# https://www.acmicpc.net/problem/1110
# 양의 정수 N 각 자리가 등차수열을 이룬다면 그 수는 등차수열
# N이 주어졌을 때 1보다 크거나 같고, N보다 작거나 같은 한수의 개수 출력

N = input()
N_list = list(map(int, str(N)))
sum_cycle = ""
cnt = 0


while True:
    if N == sum_cycle:
        break
    if len(N) > 1:
        sum_cycle = str(N_list[len(N_list)-1]) + str(sum(N_list)).strip()[-1]
        N_list = list(map(int, str(sum_cycle)))
        cnt += 1
    else:
        N = "0" + N

print(cnt)