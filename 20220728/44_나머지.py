# https://www.acmicpc.net/problem/3052
# 수 10개 입력받은 후 42로 나눈 나머지를 구한 후 서로 다른 값 몇 개 있는지 출력

nums = []

for i in range(10):
    N = int(input())
    nums.append(N%42)

print(len(set(nums)))