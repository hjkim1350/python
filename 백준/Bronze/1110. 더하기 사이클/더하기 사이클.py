N = input()
# N이 문자열로 들어오니까 list에 담길 때에는 int로 변환되도록 map함수로 처리
N_list = list(map(int, str(N)))
# N으로 다시 돌아오기까지의 중간 과정을 문자열로 담도록 함
sum_cycle = ""
# 몇번 사이클이 도는지 카운트
cnt = 0

# N이 원래의 값으로 다시 돌아왔을 때 while문을 멈추도록 함
while N != sum_cycle:
    # 두자리 숫자일땐 문제에서 요구하는 연산을 해야함
    if len(N) > 1:
        # 첫번째 자리에는 list의 두번째 요소를 가져오도록 함.
        # 두번째 자리에는 리스트에 담긴 두 수를 더한 마지막 값을 가져오도록 함.
        sum_cycle = str(N_list[len(N_list)-1]) + str(sum(N_list)).strip()[-1]
        # N의 각자리 숫자를 담고 있는 list를 int 화
        N_list = list(map(int, str(sum_cycle)))
        cnt += 1
    # 한자리 숫자일때에는 0을 앞에 붙임으로써 01, 02 등으로 표현하게 함.
    # 예를 들어 N이 1일 경우 1이라는 숫자 앞에는 0이 있다고 판단해야 함.
    # N이 1이면 0을 붙여 01이 되어 N이 두자리의 숫자로 인식하게 하여 if문으로 들어가게 함.
    else:
        N = "0" + N

print(cnt)