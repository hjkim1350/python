# https://www.acmicpc.net/problem/2902
# 긴 이름이 주어졌을 때 짧은 형태로 변환
# Input: Knuth-Morris-Pratt / Output: KMP

N = input()
short = ""

for i in N:
    if (ord(i) >= 65 and ord(i) <= 90):
        print(i, end='')