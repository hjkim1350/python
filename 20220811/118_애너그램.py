# https://www.acmicpc.net/problem/6996
# 두단어 A, B 주어졌을 때 A에 속하는 알파벳 순서 바꿔서 B 만들 수 있으면 애너그램

import sys
sys.stdin = open("test.txt")

N = int(input())

for _ in range(N):
    stc1, stc2 = input().split()
    stc1_dict = {}
    stc2_dict = {}

    for i in stc1:
        if i not in stc1_dict:
            stc1_dict.setdefault(i, 1)
        else:
            stc1_dict[i] += 1
    
    for j in stc2:
        if j not in stc2_dict:
            stc2_dict.setdefault(j, 1)
        else:
            stc2_dict[j] = stc2_dict.get(j) + 1
    
    if sorted(stc1_dict) == sorted(stc2_dict):
        print(stc1, "&", stc2, "are anagrams.")
    else:
        print(stc1, "&", stc2, "are NOT anagrams.")