# BAEKJOON 2846
# Q) 입력값 첫째줄: 상근이가 측정한 높이 수이자 수열의 크기
# 입력값 둘째줄: 양의 정수로 구성된 수열
# 둘째줄 수열에서 연속으로 증가하는 값들 중 가장 큰 값과 수열의 크기 비교

# 상근이가 측정한 높이 수이자 수열의 크기 입력받음
height = int(input())
height_start = 0
height_end = 0
height_size = []

# 양의 정수로 구성된 수열을 리스트로 입력받음
height_list = []
height_list = list(map(int, input().split()))


for i in range(1, height):

    if height_list[i] > height_list[i-1]:
        height_size.append(height_list[i-1])

        if height_list[i] == height_list[height-1]:
            height_size.append(height_list[i])
    
    else:
        height_start = height_list[i]

print(height_size)