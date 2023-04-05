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