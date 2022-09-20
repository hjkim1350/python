# https://www.acmicpc.net/problem/4949
# 긴 이름이 주어졌을 때 짧은 형태로 변환
# ( ), [ ] 등으로 이루어져있으며 . 으로 끝남
# . 만 있어도 균형을 이룬 것으로 봄.

# 엔터가 포함된 입력값 처리하기 위한 라이브러리 가져오기
import sys
# 엔터가 포함된 입력값을 lines라는 변수에 입력
# 여러줄을 입력받아 lines에 저장
lines = sys.stdin.readlines()

# 입력값 마지막 문자인 개행(\n)을 제외한 나머지를 검증하기 위해 [:-1] 범위 지정
# 여러 줄의 입력값을 하나씩 검증하기 위해 line 변수 선언
for line in lines[:-1]:
    stack = []

    # line 변수에 있는 문자열 하나씩을 t에 담아 for문 실행
    for t in line:

        # t가 (이거나 [인 경우
        if t in '([':
            # stack에 포함한다
            stack.append(t)
        # t가 ]인 경우
        elif t == "]":
            # stack에 없거나 stack에서 꺼냈을때 [이 없는 경우
            if not stack or stack.pop() != '[':
                # no를 출력하고 for문 종료
                print('no')
                break
        # t가 )인 경우
        elif t == ')':
            # stack에 없거나 stack에서 꺼냈을 때 )이 없는 경우
            if not stack or stack.pop() != '(':
                # no를 출력하고 for문 종료
                print('no')
                break
        # t가 .인 경우
        elif t == '.':
            # stack에 요소가 남아있다면 no 출력
            if stack:
                print('no')
            # stack에 요소가 없으면 yes 출력
            else:
                print("yes")