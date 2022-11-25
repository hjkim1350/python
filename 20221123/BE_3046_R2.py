# https://www.acmicpc.net/problem/3046
# 평균 S, S를 이루는 숫자 R1, R2중 R1만 주어질때 R2 값 구하기

R1, S = map(int, input().split())

print(2*S-R1)