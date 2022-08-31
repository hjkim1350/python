# https://www.acmicpc.net/problem/5063
# r은 광고하지 않았을 때 수익, e는 광고 했을때 수익, c는 광고비용
# 광고해야하면 advertise, 하지않아야하면 do not advertise, 광고해도 수익차이 없다면 does not matter

ad_list = []

for i in range(int(input())):
    r, e, c = map(int, input().split())

    if r > (e-c):
        ad_list.append("do not advertise")
    elif r < (e-c):
        ad_list.append("advertise")
    else:
        ad_list.append("does not matter")

for j in ad_list:
    print(j)