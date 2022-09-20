# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV13zo1KAAACFAYh
# 특정 자료에서 가장 많이 나타나는 값을 출력
# 첫번째 줄 테스트 케이스 수 T 주어짐
# 다음번째 줄 테스트 케이스 번호
# 그 다음 점수

# input 값 파일로 읽어들이기
import sys
sys.stdin = open("D2_1204_최빈수구하기.txt", "r")

# 테스트 케이스 수 T 처리
T = int(input())

# 테스트 케이스 수 T 만큼 반복하여 수행
for test_case in range(1, T+1):
    # 테스트 케이스 번호 처리
    test_num = int(input())

    # 점수를 int형의 리스트로 저장
    list_num = list(map(int, input().split()))

    # 0~100 점수를 포함하는 기준점 리스트 초기 선언
    score = [0]*101

    # 학생 점수를 기준점 리스트에 하나씩 카운트
    for student in list_num:
        score[student] += 1
    
    # 최빈수 여러 개일때 가장 큰 점수 출력하여야 함
    # 따라서 최빈수 동일한 경우를 대비해 max값과 동일한 값을 가진 idx 저장
    top = []
    top.append(max(score))

    for j in range(len(score)):
        if max(score) == score[j]:
            top.append(j)

    print(f"#{test_num}", top[-1])