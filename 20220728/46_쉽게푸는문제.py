# https://www.acmicpc.net/problem/1292
# 1을 한번, 2를 두번, 3을 세번 1 2 2 3 3 3 4 4 4 4 5 ...
# 이러한 수열을 만들고 어느 일정한 구간을 주면 그 구간의 합 구하기

# 문제 풀이 전략
# 수열의 위치는 n(n+1)/2, 즉 수열의 숫자는 45를 초과할 수 없음.

start_num, end_num = map(int, input().split())
list_num = []
sum = 0

# 수열 만들기
for i in range(1, end_num+1):
    for j in range(i):
        list_num.append(i)

# 수열 값 더하기
for i in range(start_num-1, end_num):
    sum += list_num[i]

print(sum)