# https://www.acmicpc.net/problem/9093
# 단어를 모두 뒤집어 출력, 단 단어의 순서는 바꿀 수 없음
# 공백 사이에 있는 단어만 순서를 변경

for i in range(int(input())):
    str_tmp = input()
    str_result = ""

    for j in str_tmp:
        if j != " ":
            str_result += j
        else:
            print(str_result[::-1], end=" ")
            str_result = ""
    print(str_result[::-1], end=" ")
    print()