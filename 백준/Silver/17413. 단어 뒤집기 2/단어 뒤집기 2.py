S = input()
stack = ''
result = ''

# tag라는 개념은 <> 있을 때 안에 단어를 뒤집기 위한 목적임
tag = False

for i in S:
    # <을 만난다던지, 공백을 만난다던지, 그 외에 단어면 뒤집어 출력
    if tag == False:
        # <을 만나면 정상적으로 출력하고 <은 stack에 넣기
        if i == '<':
            tag = True
            stack += i
        # 공백을 만나면 스택에 집어넣고 결과에도 넣어두기
        elif i == ' ':
            stack += i
            result += stack
            stack = ''
        # 그 외 단어
        else:
            stack = i + stack

    elif tag == True:
        stack += i
        if i == '>':
            tag = False
            result += stack
            stack = ''

print(result+stack)