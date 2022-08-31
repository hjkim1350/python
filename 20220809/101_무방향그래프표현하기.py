# https://www.acmicpc.net/problem/4949
# 모든 "("은 ")"와만 짝을 이뤄야함
# 모든 "["은 "]"와만 짝을 이뤄야함
# 모든 ")", "]"은 자신과 짝을 이룰 수 있는 "(", "["가 존재
# 모든 괄호들의 짝은 1:1, 괄호하나가 둘 이상의 괄호와 짝지어지지 않음
# 짝을 이루는 괄호 안의 문자열도 균형이 잡혀야함
# 문자열은 영문 알파벳, 공백, 소괄호, 대괄호로 이루어져있으며 "."로 끝남

result = []

while True:
    stc = input()
    stack = ['']

    if stc == '.':
        break
    for i in stc:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if stack[-1] == "(":
                stack.pop()
            else:
                stack.append(i)
                break
        elif i == "[":
            stack.append(i)
        elif i == "]":
            if stack[-1] == "[":
                stack.pop()
            else:
                stack.append(i)
                break
    
    if len(stack) == 1:
        result.append("YES")
    else:
        result.append("NO")

for j in result:
    print(j)