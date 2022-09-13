# https://www.acmicpc.net/problem/20001
# "고무오리 디버깅 시작": 시작
# "문제"가 주어지고 이 문제가 해결되면 "고무오리"가 주어짐
# "고무오리 디버깅 끝"으로 프로그램 끝남
# 모든 문제 해결: "고무오리야 사랑해" / 미해결 존재: "힝구"

import sys
# test.txt 파일 내용이 한글이기 때문에 encoding 설정이 필요함
sys.stdin = open("test.txt", "r", encoding="utf-8")

# 결과값 출력
result = 0

s = input()

while s != "고무오리 디버깅 끝":
    s = input()

    if s == "문제":
        result -= 1
    
    if s == "고무오리":
        if result == 0:
            result -= 2
        else:
            result += 1

if result == 0:
    print("고무오리야 사랑해")
else:
    print("힝구")