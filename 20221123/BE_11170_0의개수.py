# https://www.acmicpc.net/problem/11170
# N부터 M까지 수를 적었을 때 종이에 적힌 0 카운트
# 예를 들어 0~10이 주어지면 0과 10에 0이 1개, 총 2개

for i in range(int(input())):
    cnt = 0
    N, M = map(int, input().split())

    for j in range(N, M+1):
        if str(j).count('0') != 0:
            cnt += str(j).count('0')
    
    print(cnt)