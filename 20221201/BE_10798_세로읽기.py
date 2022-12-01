# https://www.acmicpc.net/problem/10798
# 세로로 읽은 순서대로 글을 공백없이 출력

words = []

for _ in range(5):
    words.append(input())

for j in range(15):
    for i in range(5):
        if j < len(words[i]):
            print(words[i][j], end='')