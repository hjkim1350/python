# https://www.acmicpc.net/problem/5800
# 첫째줄에는 반의 수
# 다음번 줄에는 반의 수만큼 학생수 N, 학생들의 수학점수 나열
# 출력 포맷은 다음과 같음
# Class [반번호]
# Max [최대점수], Min [최소점수], Largest gap [내림차순 시 가장 큰 인접한 점수 차이]

for i in range(int(input())):
    class_tmp = list(map(int, input().split()))
    class_num = class_tmp[0]
    score = []

    for j in range(1, class_num+1):
        score.append(class_tmp[j])
    
    score.sort(reverse=True)
    Largest_gap = []

    for h in range(len(score)-1):
        Largest_gap.append(score[h] - score[h+1])

    print("Class", i+1)
    print("Max ", score[0], ", Min ", score[len(score)-1], ", Largest gap ", max(Largest_gap), sep="")