# https://www.acmicpc.net/problem/2309
# 9개의 숫자 중 숫자 합이 100이 되는 7개의 숫자를 오름차순으로 출력
# 입력값 및 출력값은 엔터로 구분됨

mem_sum = 0
mem_list = []

for i in range(9):
    mem = int(input())
    mem_sum += mem
    mem_list.append(mem)

tmp_sum = 0

for j in range(9):
    for h in range(j+1, 9):
        tmp_sum = mem_list[j] + mem_list[h]

        if mem_sum-tmp_sum == 100:
            if h > j :
                mem_list.remove(mem_list[h])
                mem_list.remove(mem_list[j])
            else:
                mem_list.remove(mem_list[j])
                mem_list.remove(mem_list[h])
            break
    else:
        continue
    break

mem_list.sort()

for k in range(7):
    print(mem_list[k])