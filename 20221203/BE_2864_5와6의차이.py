# https://www.acmicpc.net/problem/2864
# 5를 잘못 읽을수도, 6을 잘못 읽을수도 있는 상황.
# 이 때 최소값 최대값?

A, B = input().split()
sum_min = 0
sum_max = 0

sum_min = int(A.replace("6", "5")) + int(B.replace("6", "5"))
sum_max = int(A.replace("5", "6")) + int(B.replace("5", "6"))

print(sum_min, sum_max)