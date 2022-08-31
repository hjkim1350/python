# https://www.acmicpc.net/problem/1764
# 듣도 못한 사람 N, 보도못한 사람 M에 모두 포함하는 듣보잡 이름 출력
# Input 첫째줄: N M 정수
# Input 둘째줄 ~ N+1줄: 듣도 못한 사람 명단
# Input N+2 ~ 끝: 보도 못한 사람 명단

N, M = map(int, input().split())

NM = {}

for i in range (0, N+M):
    NM_name = input()

    if NM_name not in NM:
        NM.setdefault(NM_name, 1)
    else:
        NM[NM_name] = NM.get(NM_name) + 1

NM_sort = dict(sorted(NM.items()))

NM_list = []

for key, value in NM_sort.items():
    if value > 1:
        NM_list.append(key)

print(len(NM_list))

for i in range (len(NM_list)):
    print(NM_list[i])