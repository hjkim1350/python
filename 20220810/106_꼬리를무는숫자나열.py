# https://www.acmicpc.net/problem/1598
# 2개의 정수의 간격 구하기
# 정수 표는 다음과 같음
# 1 5  9 13 17 21 25 29 ...
# 2 6 10 14 18 22 26 30 ...
# 3 7 11 15 19 23 27 31 ...
# 4 8 12 16 20 24 28 32 ...

# N1, N2 = map(int, input().split())

# # 자연수 N1, N2의 x, y 좌표를 담는 변수 선언
# N1_x = 0
# N1_y = 0
# N2_x = 0
# N2_y = 0

# # N1의 x 좌표 구하기
# if N1 % 4 != 0:
#     N1_x = (N1 // 4) + 1
# else:
#     N1_x = N1 // 4

# # N1의 y 좌표 구하기
# if N1 % 4 == 1:
#     N1_y = 1
# elif N1 % 4 == 2:
#     N1_y = 2
# elif N1 % 4 == 3:
#     N1_y = 3
# else:
#     N1_y = 4

# # N2의 x 좌표 구하기
# if N2 % 4 != 0:
#     N2_x = (N2 // 4) + 1
# else:
#     N2_x = N2 // 4

# # N2의 y 좌표 구하기
# if N2 % 4 == 1:
#     N2_y = 1
# elif N2 % 4 == 2:
#     N2_y = 2
# elif N2 % 4 == 3:
#     N2_y = 3
# else:
#     N2_y = 4

# # 결과값 출력
# print(abs(N2_x-N1_x)+abs(N2_y-N1_y))

a,b = map(int,input().split())

x,y = (a-1)//4+1,(a-1)%4
i,j = (b-1)//4+1,(b-1)%4

print(abs(x-i)+abs(y-j))