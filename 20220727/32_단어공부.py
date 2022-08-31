# https://www.acmicpc.net/problem/1157
# 알파벳 대소문자로 된 단어가 주어지면 이 단어에서 가장 많이 사용된 알파벳 구하기
# 단, 대소문자는 구분하지 않는다.
# 단, 가장 많이 사용된 알파벳이 여러 개 존재할 경우 ?을 출력

# 문제풀이 전략: 딕셔너리에 취약하므로 본 문제는 딕셔너리로 풀 것.

N = input()
N_reset = N.upper()

dic = {}
dic_value_list = []
dic_value_list_x = []
dic_value_list_x_new = []

for i in N_reset:
    # 딕셔너리 안에 해당 알파벳이 없으면 key 등록과 함께 값을 1 등록
    if i not in dic:
        dic.setdefault(i, 1)
    # 알파벳이 딕셔너리에 존재한다면 value에 +1
    else:
        dic[i] = dic.get(i) + 1

# 딕셔너리에 저장한 모든 value값만 리스트에 저장
for key, value in dic.items():
    dic_value_list.append(value)

# value가 저장된 리스트 중 중복값이 있는 경우 dic_value_list_x_new에 넣기
# dic_value_list_x는 1번만 등장한 원소를 넣는 임시 저장소임.
for i in dic_value_list:
    if i not in dic_value_list_x:
        dic_value_list_x.append(i)
    else:
        if i not in dic_value_list_x_new:
            dic_value_list_x_new.append(i)

# value 중복값이 없을 경우 딕셔너리 value 최대값 출력
if dic_value_list_x_new == []:
    print(max(dic, key=dic.get))

# value 중복값이 있을 경우 중복값이 가장 큰 값이 아닌 경우 최대값 출력
# 중복값이 가장 큰 값이 아닐 경우 해당 문자 출력
else:
    if max(dic_value_list) not in dic_value_list_x_new:
        print(max(dic, key=dic.get))
    else:
        print("?")

