# input 값 파일로 읽어들이기
import sys

sys.stdin = open("D2_1926_간단한369게임.txt", "r")

# 테스트 케이스 수 T 처리
T = int(input())

# 정답 출력 리스트
result = []

for i in range(1, T + 1):
    # 변수 선언, 문자열로 치환하는 이유: in 사용
    i = str(i)
    cnt = 0
    str_369 = ""

    # 3, 6, 9 문자열 개수 카운트
    if "3" in i:
        cnt += i.count("3")
    if "6" in i:
        cnt += i.count("6")
    if "9" in i:
        cnt += i.count("9")

    # 3, 6, 9 없으면 결과 리스트에 바로 포함
    if cnt == 0:
        result.append(i)
    # 3, 6, 9 있으면 cnt 값만큼 - 추가
    else:
        for j in range(cnt):
            str_369 += "-"
        result.append(str_369)

print(*result)
