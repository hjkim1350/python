# https://www.acmicpc.net/problem/25192
# 첫번째줄 테스트 케이스 수 T 입력
# 두번째줄부터 새로운 사람의 입장을 나타내는 ENTER, 혹은 채팅 입력 유저아이디
# 곰곰티콘이 사용된 횟수 출력\

# 하단 코드는 최초에는 user_list를 list형으로 선언하였지만,
# 정답 제출 시 백준에서 시간초과 출력
# 중복값이 없는 문제이기 때문에 user_list를 set형인 set([])으로 선언하여 해결
# 시간복잡도 x in s인 경우 list는 n(O), set은 n(1)에서 차이남

# 그리고 set은 dict와 동일한 기호인 {}을 사용하며,
# set과 dict의 차이는 {} 안에 선언되는 데이터 값에 따라 달라짐.
# 따라서 빈 값의 set을 선언하기 위해서는 set([]) 형태로 선언함

T = int(input())
cnt = 0
user_list = set([])

for _ in range(T):
    N = input()

    if N == "ENTER":
        user_list.clear()

    if N not in user_list and N !="ENTER":
        user_list.add(N)
        cnt += 1

print(cnt)