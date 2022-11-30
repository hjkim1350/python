# https://www.acmicpc.net/problem/4673
# 10000보다 작거나 같은 셀프 넘버 한줄에 하나씩 출력
# 셀프넘버란? 예를 들어 33부터 시작한다면 33+3+3=39, 39+3+9=51, ..
# 입력값은 없음

# 생성자 N을 만드는 수식
def d(n):
    n = n + sum(map(int, str(n)))
    return n

# 셀프 번호 담는 set 정의
no_self = set()

# 생성자를 set에다 넣음
for i in range(1, 10001):
    no_self.add(d(i))

# 생성자가 아니면 한줄씩 출력
for j in range(1, 10001):
    if j not in no_self:
        print(j)