# https://www.acmicpc.net/problem/2693
# 배열 중 3번째 큰 값 구하기

for i in range(int(input())):
    result_list = list(map(int, input().split()))
    result_list.sort(reverse=True)
    print(result_list[2])