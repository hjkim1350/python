# https://www.acmicpc.net/problem/14467
# 첫번째정수: 소 번호 / 두번째정수: 길 왼쪽 0 길 오른쪽 1
# 같은 번호의 소가 길을 건넌 것이 몇번인지 카운트

N = int(input())
dict = {}
cow_cross_cnt = 0

for i in range(N):
    cow, cross = map(int, input().split())

    if cow not in dict:
        dict.setdefault(cow, cross)
    else:
        if dict.get(cow) == cross:
            continue
        else:
            dict[cow] = cross
            cow_cross_cnt += 1

print(cow_cross_cnt)