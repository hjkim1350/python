# https://www.acmicpc.net/problem/7785
# 현재 회사에 있는 모든 사람 구하기.
# enter인 경우 출근, leave인 경우 퇴근. 동명이인은 없는 것으로 가정.

N = int(input())
member = {}
member_sort = {}

for i in range(N):
    name, work = input().split()
    if work == "leave":
        member.pop(name)
    else:
        member.setdefault(name, work)

member_sort = dict(sorted(member.items(), reverse=True))

for mem in member_sort.keys():
    print(mem, end=' ')