# https://www.acmicpc.net/problem/2851
# 버섯을 순서대로 집으려 함
# 모든 버섯을 집을 필요 없고 중간에 중단할 수 있음
# 첫번째부터 중단하면 모든 버섯을 먹을 수 없음
# 받은 점수의 합을 최대한 100에 가깝게 만들려함
# 만약 100에 가까운 수가 2개라면(ex 98, 102) 마리오는 큰 값을 선택

sum = 0

for _ in range(10):
    N = int(input())
    sum += N

    if sum >= 100:
        if sum - 100 > abs((sum-N) - 100):
            print(sum-N)
            break
        elif sum - 100 == abs((sum-N) - 100):
            print(sum)
            break
        else:
            print(sum)
            break

# 10번의 루틴을 다 돌았음에도 sum이 100을 넘기지 않았을 경우
if sum < 100:
    print(sum)