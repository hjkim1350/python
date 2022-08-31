# https://www.acmicpc.net/problem/2941
# 크로아티아 알파벳이 입력되는데, 알파벳 소문자와 '-', '='로만 이루어져있음
# 입력된 크로아티아 알파벳 개수 출력, 중복은 제외

N = input()
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = 0

for i in range(len(N)-1):
    if N.count(croatia[i]) > 0:
        cnt += N.count(croatia[i])
    else:
        cnt += 1

print(cnt)