# https://www.acmicpc.net/problem/1037
# 첫째줄: 약수의 개수
# 둘째줄: N의 모든 약수일때 N 구하기

nums = int(input())
nums_list = list(map(int, input().split()))

if nums == 1:
    print(nums_list[0]*nums_list[0])
else:
    nums_list.sort()
    print(nums_list[len(nums_list)-1]*nums_list[0])