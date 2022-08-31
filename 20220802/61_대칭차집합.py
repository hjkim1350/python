# https://www.acmicpc.net/problem/1269
# 2개 집합 A, B가 있을 때 (A-B), (B-A)의 합집합을 대칭차집합
# Input 첫째줄 A의 원소개수, B의 원소개수가 빈칸을 기준으로 주어짐
# Input 둘째줄 A의 모든 원소
# Input 셋째줄 B의 모든 원소

A, B = map(int, input().split())
A_set = set()
B_set = set()

A_set.update(input().split())
B_set.update(input().split())

print(len((A_set-B_set) | (B_set-A_set)))