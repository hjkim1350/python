# https://www.acmicpc.net/problem/2776
# 첫번째줄 테스트 케이스 수 T 입력
# 두번째줄 수첩1에 적어놓은 정수의 개수 N 입력
# 세번째줄 수첩1에 적어놓은 N개의 정수 입력
# 네번째줄 수첩2에 적어놓은 정수의 개수 M 입력
# 다섯번째줄 수첩2에 적어놓은 M개의 정수 입력

T = int(input())

for _ in range(T):
    N = int(input())
    N_list = set(map(int, input().split()))
    M = int(input())
    M_list = list(map(int, input().split()))
    
    for i in M_list:
        if i in N_list:
            print(1)
        else:
            print(0)