# https://www.acmicpc.net/problem/2587
# 주어진 5개 자연수의 평균과 중앙값 구하기

n_list = []

for i in range(5):
    n_list.append(int(input()))
    n_list.sort()

print(sum(n_list)//5)
print(n_list[2])