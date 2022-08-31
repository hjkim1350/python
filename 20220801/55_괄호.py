# https://www.acmicpc.net/problem/9012
# 완벽한 괄호일때만 YES, 아니면 NO를 출력
# 예를 들어 ()는 YES, ())는 NO

T = int(input())
VPS_list = []

for i in range(T):
    VPS = input()
    cnt = 0
    
    if VPS[len(VPS)-1] == "(":
        VPS_list.append("NO")
    elif VPS[0] == ")":
        VPS_list.append("NO")
    else:
        for j in VPS:
            if j == '(':
                cnt += 1
            else:
                cnt -= 1

            if cnt < 0:
                break
        
        if cnt == 0:
            VPS_list.append("YES")
        else:
            VPS_list.append("NO")

for h in range(len(VPS_list)):
    print(VPS_list[h])