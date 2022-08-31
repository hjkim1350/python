# https://www.acmicpc.net/problem/1526
# 주어진 N보다 작거나 같은 자연수 중 4, 7로만 이루어진 가장 큰 수

N = input()
gd = int('7' * len(N))

print(gd, type(gd))

if int(N) >= gd:
    print(gd)
else:
    while int(N) < gd:
        gd = str(gd)
        gd = int(gd.replace(gd[len(gd)-1], '4'))
      
        if gd == int('4' * len(N)):
            gd = int('7' * len(N)-1)
      
    print(gd)