# https://www.acmicpc.net/problem/1436
# 몇 번째 종말의 숫자 666이 나오는지 출력

N = int(input())

nums = 666

while N != 0:
    if '666' in str(nums):
        N -= 1

        if N == 0:
            break
    
    nums += 1

print(nums)