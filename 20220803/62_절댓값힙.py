# https://www.acmicpc.net/problem/11286
# 정수 x 입력받아 0이 아니면 배열에 x 값 추가
# 정수 x가 0이면 가장 작은 절대값 출력하고 배열에서 그 값 제거
# 정수 x가 0이지만 배열이 비어있으면 0을 출력

import heapq
heap = []
result = []

for i in range(int(input())):
    x = int(input())

    # 정수 x가 0이 아니면 배열에 x값 추가
    if x != 0:
        heapq.heappush(heap, x)

    else:
        # 정수 x가 0이면 가장 작은 절대값 출력하고 그 값을 제거
        if len(heap):
            print(heap, heapq.heappop(heap))
            result.append(heapq.heappop(heap))

        # 정수 x가 0이라도 배열이 비어있는 경우 0을 출력

        else:
            result.append(0)

print("------------------------------------")

for j in result:
    print(j)