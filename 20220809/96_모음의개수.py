# https://www.acmicpc.net/problem/1264
# 문장을 입력받아 모음 개수 세기 (대소문자 모두 포함)

result = []

while True:
    stc = input().lower()
    cnt = 0
    if stc == '#':
        break
    
    for ch in stc:
        if ch in ['a', 'e', 'i', 'o', 'u']:
            cnt += 1
    
    result.append(cnt)

print(*result, sep='\n')