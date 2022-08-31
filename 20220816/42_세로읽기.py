# https://www.acmicpc.net/problem/10798
# 2중 배열의 세로읽기

import sys
sys.stdin = open("test.txt")

words = []

for i in range(5):
    word = input()

    for j in word:
        words.append([j])

        

print(words)