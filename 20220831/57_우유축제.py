# https://www.acmicpc.net/problem/14720
# 영학이의 우유 마시는 규칙
# 1) 맨 처음에는 딸기우유를 1팩 마심
# 2) 딸기우유 1팩 마신 후 초코우유 1팩 마심
# 3) 초코우유 1팩 마신 후 바나나우유 1팩 마심
# 4) 바나나우유 1팩 마신 후 딸기우유 1팩 마심
# 축제가 열리는 우유 거리 시작부터 끝까지 우유를 사먹고자 하며,
# 우유 가게에서 사마실 수 있고 안마실 수도 있음. 한번 지나친 가게는 다시 돌아가지 않음
# 영학이가 마실 수 있는 우유의 최대 개수 구하기

# 우유 가게 수 N 입력 받음
N = int(input())

# 우유 가게 정보를 list로 입력 받음
store_list = list(map(int, input().split()))

# 우유 개수 카운트
cnt = 0

# 0: 딸기우유 가게 / 1: 초코우유 가게 / 2: 바나나우유 가게
# 이 외의 정수는 없음
for i in range(len(store_list)):
    if store_list[i] == 0:
        if i > 0:
            if store_list[i-1] == 2:
                cnt += 1
            else:
                i += 1
        else:
            cnt += 1
    elif store_list[i] == 1:
        if i > 0:
            if store_list[i-1] == 0:
                cnt += 1
        else:
            i += 1
    elif store_list[i] == 2:
        if i > 1:
            if (store_list[i-1] == 1 and store_list[i-2] == 0):
                cnt += 1
        else:
            i += 1

print(cnt)

## 해당 문제 1 1 0 2 1 일때 0 다음 2는 건너 뛰고 1을 카운트해야하는 로직 추가필요