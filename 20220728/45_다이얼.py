# https://www.acmicpc.net/problem/5622
# 문자열을 다이얼 전화기로 전화거는 시간 구하기
# 1을 걸려면 2초 필요하며 한칸 옆에 있는 숫자를 걸기 위해 1초 더 걸림
# ASCII를 이용하여 문자를 숫자로 치환하여 숫자 범위를 활용.

dial = input()
times = 0

for i in dial:
    if ord(i) > 86:
        times += 10
    elif ord(i) > 83:
        times += 9
    elif ord(i) > 79:
        times += 8
    elif ord(i) > 76:
        times += 7
    elif ord(i) > 73:
        times += 6
    elif ord(i) > 70:
        times += 5
    elif ord(i) > 67:
        times += 4
    else:
        times += 3

print(times)
