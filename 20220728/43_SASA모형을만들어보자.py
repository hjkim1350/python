# https://www.acmicpc.net/problem/23825
# SASA 모형을 만들기 위해 S모양 블록 2개, A모양 블록2개가 필요
# 만들 수 있는 SASA 모형 개수의 최대값 구하기

S, A = map(int, input().split())

print(S//2 if S < A else A//2)