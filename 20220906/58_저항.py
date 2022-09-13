# https://www.acmicpc.net/problem/1076
# 첫번째 색상값, 두번째색상값은 그대로 출력, 마지막색상값은 곱하기

# 입력값 출력 변수
N1 = input()
N2 = input()
N3 = input()

# 결과값 출력 변수
result = ''

# 첫번째 색, 두번째 색의 값 매칭
value_list = {'black': '0', 'brown':'1', 'red':'2', 'orange':'3',
    'yellow':'4', 'green':'5', 'blue':'6', 'violet': '7', 'grey':'8', 'white':'9'
}

# 세번째 색
mul_list = {'black': 1, 'brown':10, 'red':100, 'orange':1000,
    'yellow':10000, 'green':100000, 'blue':1000000, 'violet': 10000000,
    'grey':100000000, 'white':1000000000
}

result = int(value_list[N1] + value_list[N2])*mul_list[N3]
print(result)