# https://www.acmicpc.net/problem/2592
# 주어진 10개의 자연수의 평균과 최빈값 구하기

dict = {}
sum = 0

for i in range(10):
    T = int(input())
    sum += T
    if T not in dict:
        dict[T] = 1
    else:
        dict[T] += 1

print(sum//10)
print(max(dict, key=dict.get))