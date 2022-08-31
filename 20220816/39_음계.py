# https://www.acmicpc.net/problem/2920
# 주어진 문자열 내 오타 지우고 출력하기
# 첫 숫자는 창영이가 오타낸 위치, 두번째 문자열은 창영이가 입력한 문자열

# 출제자가 낸 의도가 아닌것 같긴한데..
# 8자리의 숫자가 1번씩 모두 나오고, 차례로 증가하는 케이스나 차례로 감소하는 케이스는 1개
# 그래서 하기와 같이 문자열 비교로도 처리가 가능한듯함.
mus = input()

if mus == '1 2 3 4 5 6 7 8':
    print("ascending")
elif mus == '8 7 6 5 4 3 2 1':
    print("descending")
else:
    print("mixed")