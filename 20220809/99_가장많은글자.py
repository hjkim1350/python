# https://www.acmicpc.net/problem/1371
# 주어진 문장에 가장 많은 알파벳 출력

# 딕셔너리 선언
dict = {}

# 입력값 처리 - 입력값은 몇줄이 입력될지 모르므로 while 처리
while True:
    # EOF 처리하기 위한 try-except 구문 작성
    try:
        stc = input()
        stc = stc.replace('\n', '')
        stc = stc.replace(' ', '')

        # VS코드 구동용: # 입력하면 입력 종료되도록 처리
#        if stc == '#':
#            break

        for i in stc:
            if i not in dict:
                dict.setdefault(i, 1) # dict = {'a': 1}
            else:
                dict[i] = dict.get(i) + 1 # dict = {'a': 2}
    except:
        break

dict_list = [m for m, n in dict.items() if max(dict.values()) == n]
dict_list.sort()
print(*dict_list, sep='')