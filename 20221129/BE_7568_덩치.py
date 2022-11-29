# https://www.acmicpc.net/problem/7568
# (몸무게, 키) 주어졌을 때 덩치 순서를 출력
# 단 몸무게는 큰데 키는 작은 경우 비교 불가이므로 순서 동일

# 풀이 전략
# (몸무게, 키)는 2중 리스트 형태로 받음.
# 등수는 1등부터 가고 차례대로 비교함.
# 차례대로 비교하고 (몸무게, 키)가 모두 큰 경우 등수를 +1

N = int(input())
nums = []

for _ in range(N):
    nums.append(input().split())

for i in range(N):
    score = 1

    for j in range(N):
        if nums[i][0] < nums[j][0] and nums[i][1] < nums[j][1]:
            score += 1
    print(score, end=" ")